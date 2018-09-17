import graphene
from graphene_django import DjangoObjectType

import datetime
from itertools import chain

from ..models import ProjectTaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo

from backend_challenge_api.users.schema import UserType
from app_projects.schema import ProjectType
from .task_schema import TaskMultipleType, TaskOpenType, TaskYesOrNoType

class BaseProjectTaskType(graphene.Interface):
  id = graphene.Int()
  status = graphene.Boolean()
  submitted_by = graphene.Field(UserType)
  project = graphene.Field(ProjectType)

class ProjectTaskMultipleType(DjangoObjectType):
  task = graphene.Field(TaskMultipleType)
  options = graphene.String()

  class Meta:
    model = ProjectTaskMultiple
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskOpenType(DjangoObjectType):
  task = graphene.Field(TaskOpenType)
  class Meta:
    model = ProjectTaskOpen
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskYesOrNoType(DjangoObjectType):
  task = graphene.Field(TaskYesOrNoType)
  class Meta:
    model = ProjectTaskYesOrNo
    interfaces = [ BaseProjectTaskType ]

class AllProjectTask(graphene.ObjectType):
  all_project_tasks = graphene.List(BaseProjectTaskType, projectid = graphene.ID())

  def resolve_all_project_tasks(self, info, projectid=None, **kwargs):

    multi_project_tasks = ProjectTaskMultiple.objects.filter(project_id = projectid)
    yes_no_project_tasks = ProjectTaskYesOrNo.objects.filter(project_id = projectid)
    open_project_tasks = ProjectTaskOpen.objects.filter(project_id = projectid)

    all_tasks = sorted(
      chain(
        multi_project_tasks, 
        yes_no_project_tasks, 
        open_project_tasks
      ),key=lambda instance: instance.task.order)

    return all_tasks


class UpdateProjectTaskMultiple(graphene.Mutation):
  # project = graphene.Field(UserType)
  task = graphene.Field(TaskMultipleType)
  project = graphene.Field(ProjectType)
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()
  status = graphene.Boolean()
  submitted_by = graphene.Field(UserType)
  pass
  
  class Arguments:
    task_id = graphene.ID(required=True)
    status = graphene.Boolean()
    project_id = graphene.ID(required=True)

  def mutate(self, info, task_id, project_id, status):
    current_user = info.context.user
    if current_user.is_anonymous:
      raise Exception('You must be logged to vote!')
    
    open_task = ProjectTaskMultiple.objects.filter(task_id=task_id, project_id=project_id).first()
    if not open_task:
      raise Exception('Invalid Link!')

    open_task.status = status
    open_task.submitted_by = current_user
    if open_task.first_touched == None:
      open_task.first_touched = datetime.datetime.now()
    open_task.count_touched += 1
    open_task.save()

    return UpdateProjectTaskMultiple(
      project = open_task.project,
      status = open_task.status,
      submitted_by = open_task.submitted_by,
      task = open_task.task,
      first_touched = open_task.first_touched,
      last_touched = open_task.last_touched,
      count_touched = open_task.count_touched
    )

class Mutation(graphene.ObjectType):
    update_project_task_multiple = UpdateProjectTaskMultiple.Field()


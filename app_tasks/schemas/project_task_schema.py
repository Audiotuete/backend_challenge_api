import graphene
import datetime
from graphene_django import DjangoObjectType

from ..models import ProjectTask
from .user_schema import UserType
from .task_schema import TaskMultipleType


class ProjectTaskType(DjangoObjectType):
  class Meta:
    model = ProjectTask

class Query(object):
  user_tasks = graphene.List(ProjectTaskType)

  def resolve_user_tasks(self, info, **kwargs):
    return ProjectTask.objects.all()

class UpdateProjectTask(graphene.Mutation):
  project = graphene.Field(UserType)
  task = graphene.Field(TaskMultipleType)
  task_value = graphene.Int()
  task_note = graphene.String()
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()
  pass
  
  class Arguments:
    task_id = graphene.Int(required=True)
    task_value = graphene.Int(required=True)
    task_note = graphene.String(required=True)

  def mutate(self, info, task_id, task_value, task_note):
    auth_user = info.context.user
    if auth_user.is_anonymous:
      raise Exception('You must be logged to vote!')
    
    task = ProjectTask.objects.filter(task_id=task_id, project_id=project.id).first()
    if not task:
      raise Exception('Invalid Link!')
    
    if not task_value <= 2 and task_value >= -1:
      raise Exception('Answer_value range is from -1 to 2')
    
    task.task_value = task_value
    task.task_note = task_note
    if task.first_touched == None:
      task.first_touched = datetime.datetime.now()
    task.count_touched += 1
    task.save()

    return UpdateProjectTask(
      project = task.project,
      task = task.task,
      task_value = task.task_value,
      task_note = task.task_note,
      first_touched = task.first_touched,
      last_touched = task.last_touched,
      count_touched = task.count_touched
    )

class Mutation(graphene.ObjectType):
    update_user_task = UpdateProjectTask.Field()


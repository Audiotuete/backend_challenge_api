import graphene
import datetime

# Types
from backend_challenge_api.users.graphql.__types import UserType
from app_tasks.graphql.__types import TaskMultipleType
from app_projects.graphql.__types import ProjectType

# Models
from ..models import ProjectTaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo



class UpdateProjectTaskMultipleMutation(graphene.Mutation):
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
      raise Exception('You must be logged to do this!')
    
    open_task = ProjectTaskMultiple.objects.filter(task_id=task_id, project_id=project_id).first()
    if not open_task:
      raise Exception('Invalid Link!')

    open_task.status = status
    open_task.submitted_by = current_user
    if open_task.first_touched == None:
      open_task.first_touched = datetime.datetime.now()
    open_task.count_touched += 1
    open_task.save()

    return UpdateProjectTaskMultipleMutation(
      project = open_task.project,
      status = open_task.status,
      submitted_by = open_task.submitted_by,
      task = open_task.task,
      first_touched = open_task.first_touched,
      last_touched = open_task.last_touched,
      count_touched = open_task.count_touched
    )

class UpdateProjectTaskMultiple(graphene.ObjectType):
    update_project_task_multiple = UpdateProjectTaskMultipleMutation.Field()


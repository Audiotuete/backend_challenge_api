import graphene
from graphql_jwt.decorators import login_required

import datetime

# Types
from backend_challenge_api.users.graphql.__types import UserType
from app_tasks.graphql.__types import TaskProblemType
from app_projects.graphql.__types import ProjectType

# Models
from ..models import ProjectTaskProblem


class UpdateProjectTaskProblemMutation(graphene.Mutation):
  # project = graphene.Field(UserType)
  task = graphene.Field(TaskProblemType)
  project = graphene.Field(ProjectType)
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()
  status = graphene.Boolean()
  submitted_by = graphene.Field(UserType)
  # description = graphene.String()
  keywords = graphene.String()
  pass
  
  class Arguments:
    task_id = graphene.ID(required=True)
    status = graphene.Boolean()
    # description = graphene.String()
    keywords = graphene.String()

  @login_required
  def mutate(self, info, task_id, status, keywords=""):
    current_user = info.context.user
    project_id = current_user.currentProject.id
    
    open_task = ProjectTaskProblem.objects.get(task_id=task_id, project_id=project_id)
    if not open_task:
      raise Exception('Invalid Link!')

    open_task.status = status
    # open_task.description = description
    open_task.keywords = keywords

    open_task.submitted_by = current_user
    
    if open_task.first_touched == None:
      open_task.first_touched = datetime.datetime.now()
    open_task.count_touched += 1
    open_task.save()

    return UpdateProjectTaskProblemMutation(
      project = open_task.project,
      status = open_task.status,
      submitted_by = open_task.submitted_by,
      task = open_task.task,
      first_touched = open_task.first_touched,
      last_touched = open_task.last_touched,
      count_touched = open_task.count_touched,
      # description = open_task.description,
      keywords = open_task.keywords,
    )

class UpdateProjectTaskProblem(graphene.ObjectType):
    update_project_task_problem = UpdateProjectTaskProblemMutation.Field()


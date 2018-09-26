import graphene
from graphql_jwt.decorators import login_required

import datetime

# Types
from backend_challenge_api.users.graphql.__types import UserType
from app_tasks.graphql.__types import TaskActionType
from app_projects.graphql.__types import ProjectType

# Models
from ..models import ProjectTaskAction


class UpdateProjectTaskActionMutation(graphene.Mutation):
  # project = graphene.Field(UserType)
  task = graphene.Field(TaskActionType)
  project = graphene.Field(ProjectType)
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()
  status = graphene.Boolean()
  submitted_by = graphene.Field(UserType)
  # description = graphene.String()
  action_1 = graphene.String()
  action_2 = graphene.String()
  action_3 = graphene.String()
  pass
  
  class Arguments:
    task_id = graphene.ID(required=True)
    status = graphene.Boolean()
    # description = graphene.String(required=False)
    action1 = graphene.String(required=False)
    action2 = graphene.String(required=False)
    action3 = graphene.String(required=False)

  @login_required
  def mutate(self, info, task_id, status, action1="", action2="", action3=""):
    current_user = info.context.user
    project_id = current_user.currentProject.id
    
    open_task = ProjectTaskAction.objects.get(task_id=task_id, project_id=project_id)
    if not open_task:
      raise Exception('Invalid Link!')

    open_task.status = status
    # open_task.description = description
    open_task.action_1 = action1
    open_task.action_2 = action2
    open_task.action_3 = action3
    open_task.submitted_by = current_user



    if action1 != "" and action2 != "" and action3 != "":
      open_task.status = True
    
    if open_task.first_touched == None:
      open_task.first_touched = datetime.datetime.now()
    open_task.count_touched += 1
    open_task.save()

    return UpdateProjectTaskActionMutation(
      project = open_task.project,
      status = open_task.status,
      submitted_by = open_task.submitted_by,
      task = open_task.task,
      first_touched = open_task.first_touched,
      last_touched = open_task.last_touched,
      count_touched = open_task.count_touched,
      # description = open_task.description,
      action_1 = open_task.action_1,
      action_2 = open_task.action_2,
      action_3 = open_task.action_3,
    )

class UpdateProjectTaskAction(graphene.ObjectType):
    update_project_task_action = UpdateProjectTaskActionMutation.Field()


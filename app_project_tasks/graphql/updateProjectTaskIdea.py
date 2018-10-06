import graphene
from graphql_jwt.decorators import login_required

import datetime

# Types
from backend_challenge_api.users.graphql.__types import UserType
from app_tasks.graphql.__types import TaskIdeaType
from app_projects.graphql.__types import ProjectType

# Models
from ..models import ProjectTaskIdea


class UpdateProjectTaskIdeaMutation(graphene.Mutation):
  # project = graphene.Field(UserType)
  task = graphene.Field(TaskIdeaType)
  project = graphene.Field(ProjectType)
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()
  status = graphene.Boolean()
  submitted_by = graphene.Field(UserType)
  # description = graphene.String()
  hashtag_1 = graphene.String()
  hashtag_2 = graphene.String()
  hashtag_3 = graphene.String()
  pass
  
  class Arguments:
    task_id = graphene.ID(required=True)
    status = graphene.Boolean()
    # description = graphene.String(required=False)
    hashtag1 = graphene.String(required=False)
    hashtag2 = graphene.String(required=False)
    hashtag3 = graphene.String(required=False)

  @login_required
  def mutate(self, info, task_id, status, hashtag1="", hashtag2="", hashtag3=""):
    current_user = info.context.user
    project_id = current_user.currentProject.id
    
    open_task = ProjectTaskIdea.objects.get(task_id=task_id, project_id=project_id)
    if not open_task:
      raise Exception('Invalid Link!')

    open_task.submitted_by = current_user

    open_task.hashtag_1 = hashtag1
    open_task.hashtag_2 = hashtag2
    open_task.hashtag_3 = hashtag3

    if hashtag1 and hashtag2 and hashtag3:
      open_task.status = True
    else:
      open_task.status = False   
    
    if open_task.first_touched == None:
      open_task.first_touched = datetime.datetime.now()
    open_task.count_touched += 1
    open_task.save()

    return UpdateProjectTaskIdeaMutation(
      project = open_task.project,
      status = open_task.status,
      submitted_by = open_task.submitted_by,
      task = open_task.task,
      first_touched = open_task.first_touched,
      last_touched = open_task.last_touched,
      count_touched = open_task.count_touched,
      # description = open_task.description,
      hashtag_1 = open_task.hashtag_1,
      hashtag_2 = open_task.hashtag_2,
      hashtag_3 = open_task.hashtag_3,
    )

class UpdateProjectTaskIdea(graphene.ObjectType):
    update_project_task_idea = UpdateProjectTaskIdeaMutation.Field()


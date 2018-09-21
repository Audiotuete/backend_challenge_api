import graphene
import graphql_jwt

from app_tasks.graphql.task_schema import AllTasks, TaskMultipleType, TaskOpenType, TaskYesOrNoType

from backend_challenge_api.users.graphql.schema import AllUsers
from backend_challenge_api.users.graphql.schema import Mutation as UserMutation

from app_projects.graphql.schema import AllProjects
from app_projects.graphql.schema import Mutation as ProjectMutation

# from app_project_tasks.graphql import AllProjectTasks
from app_project_tasks.graphql.allProjectTasks import AllProjectTasks
from app_project_tasks.graphql.updateProjectTask__ import UpdateProjectTaskMultiple


class Queries(
  AllUsers,
  # AllTasks,
  AllProjects,
  AllProjectTasks,
# -----------------------
  graphene.ObjectType
):
  pass

class Mutations(
  UserMutation,
  UpdateProjectTaskMultiple,
  ProjectMutation,
# -----------------------
  graphene.ObjectType
):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(
  query = Queries, 
  types = [
    TaskMultipleType, 
    TaskOpenType, 
    TaskYesOrNoType, 
  ],
  mutation = Mutations)
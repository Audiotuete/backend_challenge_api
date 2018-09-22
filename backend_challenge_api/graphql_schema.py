import graphene
import graphql_jwt

from app_tasks.graphql.__types import TaskMultipleType, TaskOpenType, TaskYesOrNoType
# from app_tasks.graphql.allTasks import AllTasks

from backend_challenge_api.users.graphql.allUsers import AllUsers
from backend_challenge_api.users.graphql.createUser import CreateUser

from app_projects.graphql.allProjects import AllProjects
from app_projects.graphql.createProject import CreateProject

# from app_project_tasks.graphql import AllProjectTasks
from app_project_tasks.graphql.allProjectTasks import AllProjectTasks
from app_project_tasks.graphql.updateProjectTask__ import UpdateProjectTaskMultiple


class Queries(
  # AllTasks,
  AllUsers,
  AllProjects,
  AllProjectTasks,
# -----------------------
  graphene.ObjectType
):
  pass

class Mutations(
  CreateUser,
  CreateProject,
  UpdateProjectTaskMultiple,
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
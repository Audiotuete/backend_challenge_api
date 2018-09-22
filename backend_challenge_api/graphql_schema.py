import graphene
import graphql_jwt

from app_tasks.graphql.__types import TaskMultipleType, TaskOpenType, TaskYesOrNoType

from backend_challenge_api.users.graphql.currentUser import CurrentUser
# from backend_challenge_api.users.graphql.allUsers import AllUsers
from backend_challenge_api.users.graphql.createUser import CreateUser

from app_challenges.graphql.aChallenge import AChallenge

from app_projects.graphql.aProject import AProject
from app_projects.graphql.allProjects import AllProjects
from app_projects.graphql.joinProject import JoinProject
from app_projects.graphql.createProject import CreateProject

from app_project_tasks.graphql.allProjectTasks import AllProjectTasks
from app_project_tasks.graphql.updateProjectTask__ import UpdateProjectTaskMultiple


class Queries(
  CurrentUser,
  AChallenge,
  AProject,
  # AllUsers,
  AllProjects,
  AllProjectTasks,
  # AllTasks,

# -----------------------
  graphene.ObjectType
):
  pass

class Mutations(
  CreateUser,
  CreateProject,
  JoinProject,
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
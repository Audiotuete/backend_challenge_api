import graphene
import graphql_jwt


from .schemas.task_schema import AllTasks, TaskMultipleType, TaskOpenType, TaskYesOrNoType

from backend_challenge_api.users.schema import AllUsers
from backend_challenge_api.users.schema import Mutation as UserMutation

from app_projects.schema import AllProjects
from app_projects.schema import Mutation as ProjectMutation

from .schemas.project_task_schema import AllProjectTask
from .schemas.project_task_schema import Mutation as ProjectTaskMutation


class Query(
  AllUsers,
  AllTasks,
  AllProjects,
  AllProjectTask,
  graphene.ObjectType
):
  pass

class Mutation(
  UserMutation,
  ProjectTaskMutation,
  ProjectMutation,
  graphene.ObjectType
):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, types=[TaskMultipleType, TaskOpenType, TaskYesOrNoType, ], mutation=Mutation)
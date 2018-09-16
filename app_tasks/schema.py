import graphene
import graphql_jwt


from .schemas.task_schema import AllQuesetions
from .schemas.task_schema import TaskMultipleType, TaskOpenType, TaskYesOrNoType

from .schemas.user_schema import Query as UserQuery
from .schemas.user_schema import Mutation as UserMutation
# from .schemas.user_schema import Mutation as UserMutation

from .schemas.project_task_schema import Query as UserAnswerQuery
from .schemas.project_task_schema import Mutation as UserAnswerMutation


class Query(
  UserQuery,
  AllQuesetions,
  UserAnswerQuery,
  graphene.ObjectType
):
  pass

class Mutation(
  UserMutation,
  UserAnswerMutation,
  graphene.ObjectType
):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, types=[TaskMultipleType, TaskOpenType, TaskYesOrNoType, ], mutation=Mutation)
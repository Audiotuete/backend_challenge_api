import graphene

#Types
from .__types import UserType

#Models
from ..models import User


class AllUsers(graphene.ObjectType):
  all_users = graphene.List(UserType)

  def resolve_all_users(self, info, **kwargs):
    return User.objects.all()
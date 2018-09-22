import graphene
from django.contrib.auth import get_user_model

from .__types import UserType

User = get_user_model()

# QUERYS
class AllUsers(graphene.ObjectType):
  all_users = graphene.List(UserType)

  def resolve_all_users(self, info, **kwargs):
    return User.objects.all()
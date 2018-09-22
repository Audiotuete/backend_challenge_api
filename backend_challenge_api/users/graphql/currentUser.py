from django.apps import apps as django_apps
import graphene

# Types
from .__types import UserType

# Models
from ..models import User


class CurrentUser(graphene.ObjectType):

  current_user = graphene.Field(UserType)

  def resolve_current_user(self, info, **kwargs):
    
    current_user = info.context.user

    return current_user
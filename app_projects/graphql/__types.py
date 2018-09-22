import graphene
from graphene_django import DjangoObjectType

#Models
from ..models import Project

class ProjectType(DjangoObjectType):
  class Meta:
    model = Project
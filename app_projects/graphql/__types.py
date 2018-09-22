from django.apps import apps as django_apps

import graphene
from graphene_django import DjangoObjectType

Project = django_apps.get_model('app_projects', 'Project')

class ProjectType(DjangoObjectType):
  class Meta:
    model = Project
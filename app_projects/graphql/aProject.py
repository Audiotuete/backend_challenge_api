from django.apps import apps as django_apps

import graphene
from graphql_jwt.decorators import login_required

# Types
from .__types import ProjectType

# Models
from ..models import Project


class AProject(graphene.ObjectType):

  a_project = graphene.Field(ProjectType, projectCode = graphene.String())
  
  @login_required
  def resolve_a_project(self, info, projectCode, **kwargs):
    
    match_project = Project.objects.get(project_code = projectCode)

    return match_project
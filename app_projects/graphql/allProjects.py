import graphene
from graphql_jwt.decorators import login_required

#Types
from .__types import ProjectType

#Models
from ..models import Project

class AllProjects(graphene.ObjectType):
  all_projects = graphene.List(ProjectType)

  @login_required
  def resolve_all_projects(self, info, **kwargs):
    return Project.objects.all()


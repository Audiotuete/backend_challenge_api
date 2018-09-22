import graphene

#Types
from .__types import ProjectType

#Models
from ..models import Project

class AllProjects(graphene.ObjectType):
  all_projects = graphene.List(ProjectType)

  def resolve_all_projects(self, info, **kwargs):
    return Project.objects.all()


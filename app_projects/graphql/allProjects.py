from django.apps import apps as django_apps
import graphene

from .__types import ProjectType

Project = django_apps.get_model('app_projects', 'Project')

class AllProjects(graphene.ObjectType):
  all_projects = graphene.List(ProjectType)

  def resolve_all_projects(self, info, **kwargs):
    return Project.objects.all()


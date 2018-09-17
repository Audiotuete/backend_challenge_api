from django.apps import apps as django_apps

import graphene
from graphene_django import DjangoObjectType

Project = django_apps.get_model('app_projects', 'Project')

class ProjectType(DjangoObjectType):
  class Meta:
    model = Project

# QUERYS
class AllProjects(graphene.ObjectType):
  all_projects = graphene.List(ProjectType)

  def resolve_all_projects(self, info, **kwargs):
    return Project.objects.all()

# MUTATIONS
class CreateProject(graphene.Mutation):
    project = graphene.Field(ProjectType)

    class Arguments:
        project_name = graphene.String(required=True)

    def mutate(self, info, project_name, password):
        project = django_apps.get_model('app_projects', 'Project')
        project_name=project_name
        
        project.save()

        return CreateProject(project=project)


class Mutation(graphene.ObjectType):
    create_user = CreateProject.Field()
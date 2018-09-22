import graphene

from .__types import ProjectType

class CreateProjectMutation(graphene.Mutation):
  project = graphene.Field(ProjectType)

  class Arguments:
    project_name = graphene.String(required=True)

  def mutate(self, info, project_name, password):
    project = django_apps.get_model('app_projects', 'Project')
    project_name = project_name
    
    project.save()

    return CreateProjectMutation(project=project)

class CreateProject(graphene.ObjectType):
  create_project = CreateProjectMutation.Field()
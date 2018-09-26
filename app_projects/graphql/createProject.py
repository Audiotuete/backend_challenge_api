
from django.apps import apps as django_apps

import graphene
from graphql_jwt.decorators import login_required

#Types
from .__types import ProjectType

#Models
from ..models import Project

class CreateProjectMutation(graphene.Mutation):
  project = graphene.Field(ProjectType)

  class Arguments:
    projectName = graphene.String(required=True)
    projectDescription = graphene.String(required=True)

  @login_required
  def mutate(self, info, projectName, projectDescription):
    
    currentUser = info.context.user

    Challenge = django_apps.get_model('app_challenges', 'Challenge')

    project = Project(
      project_name = projectName,
      project_description = projectDescription,
      project_creator = currentUser,
      challenge = currentUser.currentChallenge
      )

    project.save()

    currentUser.currentProject = project 
    currentUser.save()

    return CreateProjectMutation(
      project=project
      )

class CreateProject(graphene.ObjectType):
  create_project = CreateProjectMutation.Field()
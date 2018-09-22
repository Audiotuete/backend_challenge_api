import graphene
from django.apps import apps as django_apps

#Types
from .__types import ProjectType

#Models
from ..models import Project

class CreateProjectMutation(graphene.Mutation):
  project = graphene.Field(ProjectType)

  class Arguments:
    project_name = graphene.String(required=True)
    project_description = graphene.String(required=True)
    challenge_code = graphene.String(required=True)

  def mutate(self, info, projectName, projectDescription, challengeCode):
    
    currentUser = info.context.user

    Challenge = django_apps.get_model('app_challenges', 'Challenge')
    match_challenge = Challenge.objects.get(challenge_code = challengeCode) 
    

    project = Project(
      project_name = projectName,
      project_description = projectDescription,
      project_creator = currentUser,
      challenge = matchChallenge
      )

    project.save()

    currentUser.currentProject = project 
    currentUser.save()

    return CreateProjectMutation(project=project)

class CreateProject(graphene.ObjectType):
  create_project = CreateProjectMutation.Field()
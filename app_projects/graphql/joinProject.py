import graphene
from django.apps import apps as django_apps

#Types
from .__types import ProjectType

#Models
from ..models import Project

class JoinProjectMutation(graphene.Mutation):
  project = graphene.Field(ProjectType)

  class Arguments:
    projectCode = graphene.String(required=True)
    challengeCode = graphene.String(required=True)

  def mutate(self, info, projectCode, challengeCode):
    
    #Find correct Project inside correct Challenge
    Challenge = django_apps.get_model('app_challenges', 'Challenge')
    match_challenge = Challenge.objects.get(challenge_code = challengeCode) 

    project_to_join = Project.objects.get(project_code = projectCode, challenge = match_challenge)

    #Connect user to project
    currentUser = info.context.user
    currentUser.currentProject = project_to_join

    currentUser.save()

    return JoinProjectMutation(project=project_to_join)

class JoinProject(graphene.ObjectType):
  join_project = JoinProjectMutation.Field()
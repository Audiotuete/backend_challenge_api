from django.apps import apps as django_apps

import graphene
from graphql_jwt.decorators import login_required


#Types
from .__types import ProjectType

#Models
from ..models import Project

class JoinProjectMutation(graphene.Mutation):
  project = graphene.Field(ProjectType)

  class Arguments:
    projectCode = graphene.String(required=True)
  
  @login_required
  def mutate(self, info, projectCode):
    
    #Find correct Project inside correct Challenge
    Challenge = django_apps.get_model('app_challenges', 'Challenge')

    theUser = info.context.user
    theChallenge = info.context.user.currentChallenge

    project_to_join = Project.objects.filter(project_code = projectCode, challenge = theChallenge).first()

    #Connect user to project
    theUser = info.context.user
    theUser.currentProject = project_to_join

    theUser.save()

    return JoinProjectMutation(project=project_to_join)

class JoinProject(graphene.ObjectType):
  join_project = JoinProjectMutation.Field()
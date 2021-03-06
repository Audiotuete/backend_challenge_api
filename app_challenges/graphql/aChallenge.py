import graphene
from graphql_jwt.decorators import login_required

# Types
from .__types import ChallengeType

# Models
from ..models import Challenge

class AChallenge(graphene.ObjectType):

  a_challenge = graphene.Field(ChallengeType, challengeCode = graphene.String())
  
  @login_required
  def resolve_a_challenge(self, info, challengeCode, **kwargs):
    
    match_full_challenge = Challenge.objects.filter(challenge_code = challengeCode).first()

    return match_full_challenge
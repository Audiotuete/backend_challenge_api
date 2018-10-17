import graphene

# Types
from .__types import CheckChallengeType

# Models
from ..models import Challenge


class CheckChallenge(graphene.ObjectType):

  check_challenge = graphene.Field(CheckChallengeType, challengeCode = graphene.String())

  def resolve_check_challenge(self, info, challengeCode, **kwargs):
    
    match_challenge = Challenge.objects.filter(challenge_code = challengeCode).first()

    return match_challenge
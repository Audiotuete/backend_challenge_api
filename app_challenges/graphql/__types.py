
import graphene
from graphene_django import DjangoObjectType

from ..models import Challenge, ChallengeDate

class ChallengeType(DjangoObjectType):
  class Meta:
    model = Challenge

class CheckChallengeType(DjangoObjectType):
  class Meta:
    model = Challenge
    only_fields = ['id', 'challenge_code', 'context']

class ChallengeDateType(DjangoObjectType):
  class Meta:
    model = ChallengeDate
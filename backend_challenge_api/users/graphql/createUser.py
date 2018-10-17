from django.apps import apps as django_apps

import graphene
import re

#Types
from .__types import UserType

#Models
from ..models import User


class CreateUserMutation(graphene.Mutation):
  user = graphene.Field(UserType)

  class Arguments:
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    challengeCode = graphene.String(required=True)

  def mutate(self, info, username, email, password, challengeCode):
    username_lowercase = username.lower()

    if len(username) < 3:
      raise Exception('Username must have at least 3 characters!')
    if not re.match(r'(^[a-zA-Z0-9_-]+$)', username_lowercase):
      raise Exception('Username must contain only alphanumerics characters, underscores and dashes')
    if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
      raise Exception('Email must be a vaild E-Mail-Adress!')
    if len(password) < 8:
      raise Exception('The password must be at least 8 characters long!')
    if User.objects.filter(username = username_lowercase):
      raise Exception('Username already exists!')
    
    Challenge = django_apps.get_model('app_challenges', 'Challenge')
    match_challenge = Challenge.objects.filter(challenge_code = challengeCode).first()

    user = User(
      username = username_lowercase,
      email = email,
      currentChallenge = match_challenge
    )
    user.set_password(password)
    user.save()

    return CreateUserMutation(user=user)


class CreateUser(graphene.ObjectType):
  create_user = CreateUserMutation.Field()
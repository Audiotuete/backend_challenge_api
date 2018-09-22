import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .__types import UserType

# MUTATIONS
class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = get_user_model()(
            username=username
        )
        user.set_password(password)
        user.save()

        return CreateUserMutation(user=user)


class CreateUser(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
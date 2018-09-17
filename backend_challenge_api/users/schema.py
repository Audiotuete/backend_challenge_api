import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

User = get_user_model()

class UserType(DjangoObjectType):
  class Meta:
    model = User

# QUERYS
class AllUsers(graphene.ObjectType):
  all_users = graphene.List(UserType)

  def resolve_all_users(self, info, **kwargs):
    return User.objects.all()

# MUTATIONS
class CreateUser(graphene.Mutation):
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

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
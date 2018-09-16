import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from itertools import chain

from ..models import Task, TaskMultiple, TaskOpen, TaskYesOrNo

class BaseTask(graphene.Interface):
  id = graphene.Int()
  order = graphene.Int()
  question_text = graphene.String()


class TaskMultipleType(DjangoObjectType):
  options = graphene.String()
  class Meta:
    model = TaskMultiple
    interfaces = [ BaseTask ]

class TaskOpenType(DjangoObjectType):
  class Meta:
    model = TaskOpen
    interfaces = [ BaseTask ]

class TaskYesOrNoType(DjangoObjectType):
  class Meta:
    model = TaskYesOrNo
    interfaces = [ BaseTask ]

class AllQuesetions(graphene.ObjectType):
  all_questions = graphene.List(BaseTask)

  def resolve_all_questions(self, info, **kwargs):

    multi_questions = TaskMultiple.objects.all()
    yes_no_questions = TaskYesOrNo.objects.all()
    open_questions = TaskOpen.objects.all()

    all_questions = sorted(
      chain(
        multi_questions, 
        yes_no_questions, 
        open_questions
      ),key=lambda instance: instance.order)

    return all_questions


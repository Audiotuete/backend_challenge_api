import graphene
from graphene_django import DjangoObjectType

from app_tasks.models import TaskMultiple, TaskOpen, TaskYesOrNo


class BaseTaskType(graphene.Interface):
  id = graphene.Int()
  order = graphene.Int()
  task_text = graphene.String()

class TaskMultipleType(DjangoObjectType):
  options = graphene.String()
  class Meta:
    model = TaskMultiple
    interfaces = [ BaseTaskType ]

class TaskOpenType(DjangoObjectType):
  class Meta:
    model = TaskOpen
    interfaces = [ BaseTaskType ]

class TaskYesOrNoType(DjangoObjectType):
  class Meta:
    model = TaskYesOrNo
    interfaces = [ BaseTaskType ]
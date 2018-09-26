import graphene
from graphene_django import DjangoObjectType

#Models
from ..models import TaskMultiple, TaskOpen, TaskYesOrNo, TaskProblem, TaskIdea, TaskAction


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

class TaskProblemType(DjangoObjectType):
  class Meta:
    model = TaskProblem
    interfaces = [ BaseTaskType ]

class TaskIdeaType(DjangoObjectType):
  class Meta:
    model = TaskIdea
    interfaces = [ BaseTaskType ]

class TaskActionType(DjangoObjectType):
  class Meta:
    model = TaskAction
    interfaces = [ BaseTaskType ]
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from itertools import chain

from ..models import Task, TaskMultiple, TaskOpen, TaskYesOrNo

class BaseTask(graphene.Interface):
  id = graphene.Int()
  order = graphene.Int()
  task_text = graphene.String()


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
  all_tasks = graphene.List(BaseTask)

  def resolve_all_tasks(self, info, **kwargs):

    multi_tasks = TaskMultiple.objects.all()
    yes_no_tasks = TaskYesOrNo.objects.all()
    open_tasks = TaskOpen.objects.all()

    all_tasks = sorted(
      chain(
        multi_tasks, 
        yes_no_tasks, 
        open_tasks
      ),key=lambda instance: instance.order)

    return all_tasks


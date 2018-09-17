import graphene
from graphene_django import DjangoObjectType
from itertools import chain

from ..models import TaskMultiple, TaskOpen, TaskYesOrNo


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

class AllTasks(graphene.ObjectType):
  all_tasks = graphene.List(BaseTaskType)

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


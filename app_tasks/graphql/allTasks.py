import graphene
from itertools import chain

from ..models import TaskMultiple, TaskOpen, TaskYesOrNo

from .__types import BaseTaskType

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


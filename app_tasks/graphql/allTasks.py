import graphene
from graphql_jwt.decorators import login_required
from itertools import chain

#Types
from .__types import BaseTaskType

#Models
from ..models import TaskMultiple, TaskOpen, TaskYesOrNo


class AllTasks(graphene.ObjectType):
  all_tasks = graphene.List(BaseTaskType)
  
  @login_required
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


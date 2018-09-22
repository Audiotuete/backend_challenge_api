import graphene
from itertools import chain
from graphql_jwt.decorators import login_required


# Types
from .__types import BaseProjectTaskType

# Models
from ..models import ProjectTaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo


class AllProjectTasks(graphene.ObjectType):

  all_project_tasks = graphene.List(BaseProjectTaskType, projectid = graphene.ID())

  @login_required
  def resolve_all_project_tasks(self, info, projectid=None, **kwargs):

    multi_project_tasks = ProjectTaskMultiple.objects.filter(project_id = projectid)
    yes_no_project_tasks = ProjectTaskYesOrNo.objects.filter(project_id = projectid)
    open_project_tasks = ProjectTaskOpen.objects.filter(project_id = projectid)

    all_tasks = sorted(
      chain(
        multi_project_tasks, 
        yes_no_project_tasks, 
        open_project_tasks
      ),key=lambda instance: instance.task.order)

    return all_tasks
import graphene
from itertools import chain
from graphql_jwt.decorators import login_required


# Types
from .__types import BaseProjectTaskType

# Models
from ..models import ProjectTaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskProblem, ProjectTaskIdea, ProjectTaskAction


class AllProjectTasks(graphene.ObjectType):

  all_project_tasks = graphene.List(BaseProjectTaskType)

  @login_required
  def resolve_all_project_tasks(self, info, **kwargs):

    challengeId = info.context.user.currentChallenge.id

    projectId = info.context.user.currentProject.id

    # multi_project_tasks = ProjectTaskMultiple.objects.filter(project_id = projectId)
    # yes_no_project_tasks = ProjectTaskYesOrNo.objects.filter(project_id = projectId)
    # open_project_tasks = ProjectTaskOpen.objects.filter(project_id = projectId)
    problem_project_tasks = ProjectTaskProblem.objects.filter(project_id = projectId)
    idea_project_tasks = ProjectTaskIdea.objects.filter(project_id = projectId)
    action_project_tasks = ProjectTaskAction.objects.filter(project_id = projectId)


    all_tasks = sorted(
      chain(
        # multi_project_tasks, 
        # yes_no_project_tasks,
        # open_project_tasks,
        problem_project_tasks,
        idea_project_tasks,
        action_project_tasks
      ),key=lambda instance: instance.task.order)

    return all_tasks
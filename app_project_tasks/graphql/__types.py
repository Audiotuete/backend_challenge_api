import graphene
from graphene_django import DjangoObjectType

#Types
from backend_challenge_api.users.graphql.__types import UserType
from app_projects.graphql.__types import ProjectType
from app_tasks.graphql.__types import TaskMultipleType, TaskOpenType, TaskYesOrNoType, TaskProblemType, TaskIdeaType, TaskActionType

#Models
from ..models import ProjectTaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskProblem, ProjectTaskIdea, ProjectTaskAction



class BaseProjectTaskType(graphene.Interface):
  id = graphene.Int()
  status = graphene.Boolean()
  submitted_by = graphene.Field(UserType)
  project = graphene.Field(ProjectType)

class ProjectTaskMultipleType(DjangoObjectType):
  task = graphene.Field(TaskMultipleType)
  options = graphene.String()

  class Meta:
    model = ProjectTaskMultiple
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskOpenType(DjangoObjectType):
  task = graphene.Field(TaskOpenType)
  class Meta:
    model = ProjectTaskOpen
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskYesOrNoType(DjangoObjectType):
  task = graphene.Field(TaskYesOrNoType)
  class Meta:
    model = ProjectTaskYesOrNo
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskProblemType(DjangoObjectType):
  task = graphene.Field(TaskProblemType)
  class Meta:
    model = ProjectTaskProblem
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskIdeaType(DjangoObjectType):
  task = graphene.Field(TaskIdeaType)
  class Meta:
    model = ProjectTaskIdea
    interfaces = [ BaseProjectTaskType ]

class ProjectTaskActionType(DjangoObjectType):
  task = graphene.Field(TaskActionType)
  class Meta:
    model = ProjectTaskAction
    interfaces = [ BaseProjectTaskType ]
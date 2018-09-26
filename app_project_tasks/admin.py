from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskMultiple, ProjectTaskProblem, ProjectTaskIdea, ProjectTaskAction


class ProjectTaskOpenAdmin(admin.ModelAdmin):
  model = ProjectTaskOpen
  list_display = [ 'project', 'task'  ]
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class ProjectTaskYesOrNoAdmin(admin.ModelAdmin):
  model = ProjectTaskYesOrNo
  list_display = [ 'project', 'task', 'task_value', 'task_note']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class ProjectTaskMultipleAdmin(admin.ModelAdmin):
  model = ProjectTaskMultiple
  list_display = [ 'task', 'project', 'submitted_by']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class ProjectTaskProblemAdmin(admin.ModelAdmin):
  model = ProjectTaskProblem
  list_display = [ 'task', 'project', 'submitted_by']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class ProjectTaskIdeaAdmin(admin.ModelAdmin):
  model = ProjectTaskIdea
  list_display = [ 'task', 'project', 'submitted_by']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class ProjectTaskActionAdmin(admin.ModelAdmin):
  model = ProjectTaskAction
  list_display = [ 'task', 'project', 'submitted_by']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False



# admin.site.register(ProjectTaskOpen, ProjectTaskOpenAdmin)
# admin.site.register(ProjectTaskYesOrNo, ProjectTaskYesOrNoAdmin)
# admin.site.register(ProjectTaskMultiple, ProjectTaskMultipleAdmin)
admin.site.register(ProjectTaskProblem, ProjectTaskProblemAdmin)
admin.site.register(ProjectTaskIdea, ProjectTaskIdeaAdmin)
admin.site.register(ProjectTaskAction, ProjectTaskActionAdmin)
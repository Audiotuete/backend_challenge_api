from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskMultiple


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
  list_display = [ 'project', 'task', 'submitted_by']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False


admin.site.register(ProjectTaskOpen, ProjectTaskOpenAdmin)
admin.site.register(ProjectTaskYesOrNo, ProjectTaskYesOrNoAdmin)
admin.site.register(ProjectTaskMultiple, ProjectTaskMultipleAdmin)
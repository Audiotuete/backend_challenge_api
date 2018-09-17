from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import TaskOpen, TaskYesOrNo, TaskMultiple, ProjectTaskOpen, ProjectTaskYesOrNo, ProjectTaskMultiple, Task

class TaskAdmin(OrderedModelAdmin):
  model = Task
  list_display = ('task_text', 'move_up_down_links')

  def has_add_permission(self, request):
    return False
  # def has_change_permission(self, request, obj=None):
  #   return False

  def get_readonly_fields(self, request, obj=None):
    if obj:
        return [
          'task_text', 
          'task_imagelink',
          'task_videolink',
          ]
    else:
        return []

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


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskOpen)
admin.site.register(TaskYesOrNo)
admin.site.register(TaskMultiple)
admin.site.register(ProjectTaskOpen, ProjectTaskOpenAdmin)
admin.site.register(ProjectTaskYesOrNo, ProjectTaskYesOrNoAdmin)
admin.site.register(ProjectTaskMultiple, ProjectTaskMultipleAdmin)
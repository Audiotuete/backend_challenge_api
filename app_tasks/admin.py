from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import TaskOpen, TaskYesOrNo, TaskMultiple, Task

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

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskOpen)
admin.site.register(TaskYesOrNo)
admin.site.register(TaskMultiple)
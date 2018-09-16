from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import TaskOpen, TaskYesOrNo, TaskMultiple, UserAnswerOpen, UserAnswerYesOrNo, UserAnswerMultiple, Task

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

class UserAnswerOpenAdmin(admin.ModelAdmin):
  model = UserAnswerOpen
  list_display = [ 'project', 'task'  ]
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class UserAnswerYesOrNoAdmin(admin.ModelAdmin):
  model = UserAnswerYesOrNo
  list_display = [ 'project', 'task', 'answer_value', 'answer_note']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class UserAnswerMultipleAdmin(admin.ModelAdmin):
  model = UserAnswerMultiple
  list_display = [ 'project', 'task']
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskOpen)
admin.site.register(TaskYesOrNo)
admin.site.register(TaskMultiple)
admin.site.register(UserAnswerOpen, UserAnswerOpenAdmin)
admin.site.register(UserAnswerYesOrNo, UserAnswerYesOrNoAdmin)
admin.site.register(UserAnswerMultiple, UserAnswerMultipleAdmin)
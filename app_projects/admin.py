from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
  model = Project
  readonly_fields = ['project_code',]
  actions = None

  # def has_add_permission(self, request):
  #   return False
  def has_delete_permission(self, request, obj=None):
    return False

# Register your models here.
admin.site.register(Project, ProjectAdmin)

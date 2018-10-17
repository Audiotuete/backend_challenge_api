from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Project

User = get_user_model()

class ProjectMembersInline(admin.TabularInline):
  model = User
  exclude = ['currentChallenge', 'name', 'first_name', 'last_name', 'is_superuser', 
            'is_staff', 'date_joined', 'last_login', 'groups', 'password', 'user_permissions']


class ProjectAdmin(admin.ModelAdmin):
  model = Project
  readonly_fields = ['project_code',]
  list_display = [ 'project_name', 'project_creator', 'project_code', ]
  inlines = [ProjectMembersInline]


  # actions = None

  # def has_add_permission(self, request):
  #   return False
  # def has_delete_permission(self, request, obj=None):
  #   return False

# Register your models here.
admin.site.register(Project, ProjectAdmin)
from django.contrib import admin

from .models import Challenge, ChallengeDate

class ChallengeDateInline(admin.TabularInline):
  model = ChallengeDate

class ChallengeAdmin(admin.ModelAdmin):
  model = Challenge
  # readonly_fields = ['challenge_code',]
  inlines = [ChallengeDateInline]
  filter_horizontal = ('contact_info',)
  actions = None

  # def has_add_permission(self, request):
  #   return False
  def has_delete_permission(self, request, obj=None):
    return False

admin.site.register(Challenge, ChallengeAdmin)
# admin.site.register(ChallengeDate)


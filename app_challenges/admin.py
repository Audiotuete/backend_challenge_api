from django.contrib import admin
from django.contrib.auth import get_user_model

from ordered_model.admin import OrderedModelAdmin


from .models import Challenge, ChallengeDate

User = get_user_model()

class ChallengeDateAdmin(OrderedModelAdmin):
  model = ChallengeDate
  list_display = ('challenge', 'event_name', 'event_location',  'move_up_down_links', 'order')
  search_fields = ('challenge', 'order',)

class ChallengeDateInline(admin.TabularInline):
  model = ChallengeDate

class ChallengeAdmin(admin.ModelAdmin):
  model = Challenge
  # readonly_fields = ['challenge_code',]
  inlines = [ChallengeDateInline]
  fieldsets = (('Challenge', {'fields': ('context', 'city', 'year', 'start_date', 'end_date', 'challenge_code', 'contact_info' )}),)
  filter_horizontal = ('contact_info',)
  actions = None

  def formfield_for_manytomany(self, db_field, request, **kwargs):
    if db_field.name == 'contact_info':
      kwargs['queryset'] = User.objects.filter(is_challenge_contact = True)
    return super().formfield_for_manytomany(db_field, request, **kwargs)

  # def has_add_permission(self, request):
  #   return False
  def has_delete_permission(self, request, obj=None):
    return False

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(ChallengeDate, ChallengeDateAdmin)


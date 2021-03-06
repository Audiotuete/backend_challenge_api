from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from backend_challenge_api.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

CUSTOM_USER_FIELDS = (
    (None, {'fields': ('currentChallenge', 'currentProject', 'is_challenge_contact')}),
)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (('User', {'fields': ('name',)}),) + CUSTOM_USER_FIELDS + auth_admin.UserAdmin.fieldsets
    list_display = ['username', 'currentChallenge', 'currentProject', 'is_challenge_contact', 'date_joined' ]
    search_fields = ['name']

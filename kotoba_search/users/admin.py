from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .utils import delete_authors_starting_with_a

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    actions = [delete_authors_starting_with_a]

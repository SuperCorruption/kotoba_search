from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages

def delete_authors_starting_with_a(modeladmin, request, queryset):
    to_delete = queryset.filter(Username__startswith='a')
    deleted = to_delete.count()
    to_delete.delete()
    modeladmin.message_user(request, f"{deleted} author(s) starting with 'a' were deleted.")

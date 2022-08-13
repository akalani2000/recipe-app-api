# Django Admin customization

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseradmin

from core import models


class UserAdmin(BaseUseradmin):
    # Define the admin pages for users.
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)

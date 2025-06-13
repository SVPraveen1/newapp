from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        if obj.is_superuser:
            obj.role = 'admin'
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)

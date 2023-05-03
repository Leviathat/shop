from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "email"]

admin.site.register(User, UserAdmin)
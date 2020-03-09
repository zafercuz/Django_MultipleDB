from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = (
                    ('HRIS', {'fields': ('hris_id',)}),
                ) + UserAdmin.fieldsets + (
                    ('More Info', {'fields': ('bio', 'location', 'birth_date',)}),
                )


admin.site.register(User, MyUserAdmin)

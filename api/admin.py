from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Hobby

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'hobbies')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'date_of_birth', 'hobbies')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Hobby)

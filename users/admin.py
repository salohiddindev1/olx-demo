from django.contrib import admin

from users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')


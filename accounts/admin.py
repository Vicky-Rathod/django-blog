from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

@admin.register(Account)
class AccountModelAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('id', 'date_joined', 'last_login')
    list_filter = ('last_login', 'username')
    search_fields = ('username', 'email')
    filter_horizontal = ()
    fieldsets = ()

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('pk','full_name', 'date_of_birth',)
    readonly_fields = ('id', 'date_of_birth')
    # search_fields = ('username', 'email')
    # filter_horizontal = ()
    # fieldsets = ()

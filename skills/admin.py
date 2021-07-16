from django.contrib import admin
from .models import Skill
@admin.register(Skill)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ('pk','name',)
    readonly_fields = ('id',)
    # search_fields = ('username', 'email')
    # filter_horizontal = ()
    # fieldsets = ()

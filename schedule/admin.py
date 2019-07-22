from django.contrib import admin

from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'when', 'user_id', 'recipe', 'portion')
    list_display_links = ('id', 'when')

admin.site.register(Schedule, ScheduleAdmin)

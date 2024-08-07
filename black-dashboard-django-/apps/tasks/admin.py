from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assigned_to', 'office', 'status', 'due_date')
    search_fields = ('name', 'project__name', 'assigned_to__username')
    list_filter = ('status', 'project', 'assigned_to', 'office')
    date_hierarchy = 'due_date'

admin.site.register(Task, TaskAdmin)


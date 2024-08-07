# departments/admin.py
# departments/admin.py
from django.contrib import admin
from .models import Department, Office

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'tasks', 'next_department', 'created_at', 'updated_at')
    search_fields = ('name', 'description')

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'responsibilities', 'next_office', 'director', 'created_at', 'updated_at')
    search_fields = ('name', 'responsibilities')
    list_filter = ('department', 'director')



# projects/admin.py

from django.contrib import admin
from .models import Project, Contractor, ExternalWait, ProjectStatusReport

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'status', 'start_date', 'end_date', 'current_office', 
                    'next_office', 'priority', 'budget', 'contract_number', 'completion_percentage',
                    'risk_level', 'estimated_duration', 'notes')
    search_fields = ('name', 'type', 'description')
    list_filter = ('status', 'type', 'risk_level', 'current_office', 'next_office')

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'bid_amount', 'bid_date', 'contract_signed_date')
    search_fields = ('name', 'project__name')

class ExternalWaitAdmin(admin.ModelAdmin):
    list_display = ('description', 'project', 'expected_completion_date', 'status')
    search_fields = ('description', 'project__name')
    list_filter = ('status',)

class ProjectStatusReportAdmin(admin.ModelAdmin):
    list_display = ('project', 'report_date', 'status', 'comments')
    search_fields = ('project__name', 'comments')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(ExternalWait, ExternalWaitAdmin)
admin.site.register(ProjectStatusReport, ProjectStatusReportAdmin)


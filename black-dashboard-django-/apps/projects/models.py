from django.db import models
from datetime import datetime
from apps.departments.models import Office
from django_fsm import FSMField, transition

class Project(models.Model):
    STATUS_CHOICES = [
        ('initiated', 'Initiated'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(choices=(
            ('إستشارة', 'إستشارة '),
            ('صفقة', ' صفقة'),
        ),
        max_length=255,
        default='إستشارة'
    )
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)
    status = FSMField(default='initiated', choices=STATUS_CHOICES)
    priority = models.CharField(max_length=50, default='0')
    budget = models.CharField(max_length=20, default='0')
    contract_number = models.CharField(max_length=255, blank=True, null=True)
    completion_percentage = models.PositiveIntegerField(default=0)
    risk_level = models.CharField(choices=(
                    ('Low', 'Low'),
                    ('Medium', 'Medium'),
                    ('High', 'High')
                    ),
                    max_length=255,
                     default='Low'
    )
    estimated_duration = models.PositiveIntegerField(default=0)  # تم تغيير default إلى 0 بدلاً من '0'
    notes = models.TextField(blank=True, null=True)
    current_office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_projects')
    next_office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True, related_name='next_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @transition(field=status, source='initiated', target='in_progress')
    def start_project(self):
        pass

    @transition(field=status, source='in_progress', target='completed')
    def complete_project(self):
        pass

    def __str__(self):
        return self.name

class Contractor(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contractors', null=True)
    bid_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    bid_date = models.DateField(null=True, blank=True)
    contract_signed_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.project.name}'

class ExternalWait(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Delayed', 'Delayed'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='external_waits')
    description = models.TextField()
    expected_completion_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    document_path = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} - {self.project.name}'

class ProjectStatusReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='status_reports')
    report_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=190, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Report for {self.project.name} on {self.report_date}'



from django.db import models
from apps.departments.models import Office
from apps.authentication.models import CustomUser
from apps.projects.models import Project
from django_fsm import FSMField, transition

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    status = FSMField(default='pending', choices=STATUS_CHOICES)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @transition(field=status, source='pending', target='in_progress')
    def start_task(self):
        pass

    @transition(field=status, source='in_progress', target='completed')
    def complete_task(self):
        pass

    def __str__(self):
        return f'Task: {self.name} (Status: {self.status})'



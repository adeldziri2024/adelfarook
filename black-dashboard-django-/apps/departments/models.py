# departments/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    tasks = models.TextField(null=True, blank=True)
    next_department = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_departments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Office(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='offices')
    responsibilities = models.TextField(null=True, blank=True)
    next_office = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_offices')
    director = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='directed_offices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



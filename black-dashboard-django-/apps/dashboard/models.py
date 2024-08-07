# dashboard/models.py
# dashboard/models.py
from django.db import models
from apps.authentication.models import CustomUser

class DashboardData(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    office = models.ForeignKey('departments.Office', on_delete=models.SET_NULL, null=True, blank=True, related_name='dashboard_data')
    last_login = models.DateTimeField(auto_now_add=True)
    projects_count = models.IntegerField(default=0)
    tasks_count = models.IntegerField(default=0)
    upcoming_deadlines = models.ManyToManyField('tasks.Task', blank=True)
    notifications = models.ManyToManyField('notifications.Notification', blank=True)

    def __str__(self):
        return f"Dashboard Data for {self.user.username} at {self.office.name if self.office else 'Unknown Office'}"




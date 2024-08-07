# dashboard/admin.py
from django.contrib import admin
from .models import DashboardData

@admin.register(DashboardData)
class DashboardDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'office', 'last_login', 'projects_count', 'tasks_count')
    search_fields = ('user__username', 'office__name')
    list_filter = ('office',)
    ordering = ('-last_login',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # إذا كنت تريد إظهار بيانات معينة بناءً على صلاحيات المستخدم
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user=request.user)

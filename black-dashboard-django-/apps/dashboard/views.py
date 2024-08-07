# dashboard/views.py
# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.authentication.models import CustomUser
from .models import DashboardData
from apps.projects.models import Project
from apps.tasks.models import Task
from apps.notifications.models import Notification

@login_required
def office_dashboard(request):
    user_office = getattr(request.user, 'office', None)  # استخدام getattr للتحقق بأمان
    is_superuser = request.user.is_superuser

    # جلب بيانات لوحة التحكم بناءً على المكتب
    dashboard_data = DashboardData.objects.filter(user=request.user).first()

    # إعداد البيانات العامة
    projects = Project.objects.filter(current_office=request.user.office) if user_office else Project.objects.none()
    tasks = Task.objects.filter(office=request.user.office) if user_office else Task.objects.none()
    notifications = Notification.objects.all()

    # تحديد القالب بناءً على حالة المستخدم
    if is_superuser:
        template_name = 'home/superuser_dashboard.html'
        context = {
            'projects': Project.objects.all(),
            'tasks': Task.objects.all(),
            'notifications': notifications,
            'dashboard_data': dashboard_data
        }
    else:
        templates = {
            'Technical_Department': 'home/technical_dashboard.html',
            'Conventions_Office': 'home/conventions_dashboard.html',
            'Etudes_Office': 'home/etudes_dashboard.html',
            'Suivi_Office': 'home/suivi_dashboard.html',
            'Conservation_Office': 'home/conservation_dashboard.html',
            'Contracts_Department': 'home/contracts_dashboard.html',
            'Contracts_Office': 'home/contracts_office_dashboard.html',
            'Gestrealstat_Office': 'home/gestrealstat_dashboard.html',
            'Investisement_Office': 'home/investisement_dashboard.html',
            'Financial_Department': 'home/financial_dashboard.html'
        }

        template_name = templates.get(user_office.name, 'home/default_dashboard.html') if user_office else 'home/default_dashboard.html'
        context = {
            'projects': projects,
            'tasks': tasks,
            'dashboard_data': dashboard_data
        }

    return render(request, template_name, context)

def default_dashboard(request):
    # افتراضياً، يمكنك وضع منطق دالة العرض هنا
    return render(request, 'default_dashboard.html')





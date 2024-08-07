# apps/notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # أضف الروابط الخاصة بتطبيق notifications هنا
    path('notification-list/', views.notification_list, name='notification_list'),
]

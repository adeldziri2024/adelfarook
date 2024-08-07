# dashboard/urls.py
# dashboard/urls.py
from django.urls import path
from . import views  # تأكد من استيراد views هنا

urlpatterns = [
    path('default/', views.default_dashboard, name='default_dashboard'),
    path('office/', views.office_dashboard, name='office_dashboard'),
    path('superuser-dashboard/', views.office_dashboard, name='superuser_dashboard'),
    path('Conventions_Office/', views.office_dashboard, name='Conventions_Office'),
    path('Technical_Department/', views.office_dashboard, name='Technical_Department'),
    path('Etudes_Office/', views.office_dashboard, name='Etudes_Office'),
    path('Suivi_Office/', views.office_dashboard, name='Suivi_Office'),
    path('Conservation_Office/', views.office_dashboard, name='Conservation_Office'),
    path('Contracts_Department/', views.office_dashboard, name='Contracts_Department'),
    path('Contracts_Office/', views.office_dashboard, name='Contracts_Office'),
    path('Gestrealstat_Office/', views.office_dashboard, name='Gestrealstat_Office'),
    path('Investisement_Office/', views.office_dashboard, name='Investisement_Office'),
    path('Financial_Department/', views.office_dashboard, name='Financial_Department'),
    # أضف المسارات الأخرى هنا
]

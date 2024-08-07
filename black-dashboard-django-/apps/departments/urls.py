# departments/urls.py

from django.urls import path
from . import views



urlpatterns = [
    path('', views.department_list, name='departments_list'),
    path('departments/<int:department_id>/offices/', views.office_list, name='office_list'),
    path('offices/<int:office_id>/', views.office_detail, name='office_detail'),
]

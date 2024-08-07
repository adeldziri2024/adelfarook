# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
# main_project/urls.py


from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route  apps.departments
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
   # path('apps.departments/', include('apps.departments.urls')),'apps.tasks'
    path('apps.projects/', include('apps.projects.urls')),
    path('apps.tasks/', include('apps.tasks.urls')),
    path('apps.notifications/', include('apps.notifications.urls')), # Notifications routes      'apps.dashboard',
    path('apps.dashboard/', include('apps.dashboard.urls')),

	


    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
          
]

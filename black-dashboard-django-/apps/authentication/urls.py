# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test

# Decorator to restrict access to the register page to superusers only
register_user_view = user_passes_test(lambda u: u.is_superuser)(register_user)

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user_view, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
]


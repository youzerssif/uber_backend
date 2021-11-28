

from django.contrib import admin
from django.urls import path,include
from . import views

# app_name = 'admins'
urlpatterns = [
    path('', views.home, name='home'),

]
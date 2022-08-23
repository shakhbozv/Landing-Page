from django.urls import path

from . import views

urlpatterns = [
    path('', views.project, name='home'),
    path('developer/', views.developer, name='developer'),
    path('skill/', views.skill, name='skill'),
]

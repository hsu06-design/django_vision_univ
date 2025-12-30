from django.urls import path
from .views import projects_home

urlpatterns = [
    path('projects/', projects_home, name='projects_home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_home, name='projects_home'),
]
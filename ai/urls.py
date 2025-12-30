from django.urls import path
from .views import ai_home

urlpatterns = [
    path('ai/', ai_home, name='ai_home'),
]
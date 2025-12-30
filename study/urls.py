from django.urls import path
from .views import study_home

urlpatterns = [
    path('study/', study_home, name='study_home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path("study/", views.study_home, name="study_home"),
    path("projects/", views.projects_home, name="projects_home"),
]

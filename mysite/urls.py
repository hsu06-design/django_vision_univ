from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("", include("notes.urls")),
    path("", include("pages.urls")),
    path('ai/', include('ai.urls')),
    path('study/', include('study.urls')),
    path('projects/', include('projects.urls')),
]


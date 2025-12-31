from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path('notes/', include('notes.urls', namespace='notes')),
    path("", include("pages.urls")),
    path('study/', include('study.urls')),
    path('projects/', include('projects.urls')),
]


from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # blog
    path("", blog_views.post_list, name="home"),
    path("blog/", include("blog.urls")),

    # pages
    path("", include("pages.urls")),

    # notes
    path("", include("notes.urls")),
]

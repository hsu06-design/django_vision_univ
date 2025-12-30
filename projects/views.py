from django.shortcuts import render
from .models import Project

def projects_home(request):
    projects = Project.objects.all().order_by("-tech")
    return render(request, "projects/projects_home.html", {"projects": projects})

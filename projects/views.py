from django.shortcuts import render

def projects_home(request):
    # No more database queries! Just a simple render.
    return render(request, "projects/projects_home.html")
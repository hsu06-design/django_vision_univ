from django.shortcuts import render
from .models import StudyPlan

def study_home(request):
    plans = StudyPlan.objects.all().order_by("-progress")
    return render(request, "study/study_home.html", {"plans":plans})

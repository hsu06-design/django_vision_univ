from django.shortcuts import render
from .models import AIItem

def ai_home(request):
    items = AIItem.objects.all().order_by("-created_at")
    return render(request, "ai/ai_home.html", {"items": items})

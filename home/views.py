from django.shortcuts import render
from .models import HomeConfig
import requests
from collections import Counter
from django.conf import settings
from machines.models import Machine

def home_view(request):
    config = HomeConfig.objects.first()      
    machines = Machine.objects.all().values("difficulty")
    difficulties = [m["difficulty"] for m in machines if m.get("difficulty")]
    counts = Counter(difficulties)
    stats = {
        "total": len(machines),
        "easy": counts.get("Easy", 0),
        "medium": counts.get("Medium", 0),
        "hard": counts.get("Hard", 0),
    }
    context = {
        "config": config,
        "stats": stats,
    }
    return render(request, "home.html", context)

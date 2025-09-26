from django.shortcuts import render
from .models import HomeConfig
import requests
from collections import Counter
from django.conf import settings


def home_view(request):
    config = HomeConfig.objects.first()  

    api_url = f"{settings.API_BASE_URL}/machines-basic/"

    response = requests.get(api_url)
    machines = response.json() if response.status_code == 200 else []

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

from django.conf import settings

def api_base_url(request):
    return {
        "BASE_URL": settings.BASE_URL
    }

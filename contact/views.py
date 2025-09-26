from django.shortcuts import render, redirect
from .forms import ContactForm
from django_ratelimit.decorators import ratelimit
from .models import ContactMessage
from .models import ContactPage

@ratelimit(key="ip", rate="5/m", block=False)
def contact_view(request):
    page = ContactPage.objects.first() 
    if getattr(request, "limited", False):
        return render(request, "contact/too_many_requests.html")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not name or not email or not message:
            return render(request, "contact.html", {
                "error": "Todos los campos son obligatorios."
            })

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject, 
            message=message
        )
        return redirect("contact_success")

    return render(request, "contact.html", {"page": page})


def success_view(request):
    return render(request, "success.html")

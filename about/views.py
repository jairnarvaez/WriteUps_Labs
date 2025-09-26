from django.shortcuts import render
from .models import AboutPage

def about_view(request):
    about_page = AboutPage.objects.first()  
    cards_principal = about_page.cards.filter(seccion="principal")
    cards_tres = about_page.cards.filter(seccion="tres")
    cards_dos = about_page.cards.filter(seccion="dos")

    return render(request, "about.html", {
        "about_page": about_page,
        "cards_principal": cards_principal,
        "cards_tres": cards_tres,
        "cards_dos": cards_dos,
    })

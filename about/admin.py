from django.contrib import admin
from .models import AboutPage, Card

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    inlines = [CardInline]

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("titulo", "emoji", "seccion", "about_page")
    list_filter = ("seccion",)

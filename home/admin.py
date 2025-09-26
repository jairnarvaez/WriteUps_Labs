from django.contrib import admin
from .models import HomeConfig

@admin.register(HomeConfig)
class HomeConfigAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo")

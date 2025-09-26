from django.db import models

class AboutPage(models.Model):
    titulo = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10, help_text="Ejemplo: 🚀")
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class Card(models.Model):
    SECCION_CHOICES = [
        ("principal", "Card Principal"),
        ("tres", "Grupo de 3 Cards"),
        ("dos", "Grupo de 2 Cards"),
    ]

    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name="cards")
    titulo = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10, help_text="Ejemplo: 💡")
    descripcion = models.TextField()
    seccion = models.CharField(max_length=20, choices=SECCION_CHOICES)

    def __str__(self):
        return f"{self.titulo} ({self.get_seccion_display()})"

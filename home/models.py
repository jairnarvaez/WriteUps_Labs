from django.db import models

class HomeConfig(models.Model):
    titulo = models.CharField(max_length=200, default="Título por defecto")
    subtitulo = models.CharField(max_length=300, default="Subtítulo por defecto")

    # Card destacada (la de arriba)
    card_titulo = models.CharField(max_length=200)
    card_emoji = models.CharField(max_length=10, help_text="Ej: 🚀")
    card_descripcion = models.TextField()
    boton_1_texto = models.CharField(max_length=50, blank=True, null=True)
    boton_1_url = models.URLField(blank=True, null=True)
    boton_2_texto = models.CharField(max_length=50, blank=True, null=True)
    boton_2_url = models.URLField(blank=True, null=True)
    boton_3_texto = models.CharField(max_length=50, blank=True, null=True)
    boton_3_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Configuración de Home"
        verbose_name_plural = "Configuración de Home"

    def __str__(self):
        return "Configuración de la Página Principal"

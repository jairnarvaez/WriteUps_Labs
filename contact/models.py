from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class ContactPage(models.Model):
    titulo = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10, help_text="Ej: 😊")
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class PersonalInfo(models.Model):
    contact_page = models.OneToOneField(ContactPage, on_delete=models.CASCADE, related_name="personal_info")
    emoji = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    profesion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class PersonalList(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="listados")
    emoji = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)  # Ej: "Lenguajes", "Frameworks"
    
    def __str__(self):
        return f"{self.tipo}"


class PersonalListItem(models.Model):
    listado = models.ForeignKey(PersonalList, on_delete=models.CASCADE, related_name="items")
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Objective(models.Model):
    contact_page = models.OneToOneField(ContactPage, on_delete=models.CASCADE, related_name="objetivo")
    emoji = models.CharField(max_length=10)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class ObjectiveSubsection(models.Model):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name="subsecciones")
    emoji = models.CharField(max_length=10)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class PersonalProject(models.Model):
    contact_page = models.ForeignKey(ContactPage, on_delete=models.CASCADE, related_name="proyectos")
    emoji = models.CharField(max_length=10)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField()
    version = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=[("En progreso","En progreso"),("Terminado","Terminado")])
    color_background = models.CharField(max_length=150, default="gray")  # Tailwind color, ej: "blue", "green"
    color_emoji = models.CharField(max_length=150, default="gray")  # Tailwind color, ej: "blue", "green"
    color_border = models.CharField(max_length=150, default="gray")  # Tailwind color, ej: "blue", "green"
    color_title = models.CharField(max_length=150, default="gray")  # Tailwind color, ej: "blue", "green"
    color_technology = models.CharField(max_length=150, default="gray")  # Tailwind color, ej: "blue", "green"
    color_technology_background = models.CharField(max_length=150, default="gray")  # Tailwind color, ej: "blue", "green"
    
    def __str__(self):
        return self.titulo


class ProjectTechnology(models.Model):
    proyecto = models.ForeignKey(PersonalProject, on_delete=models.CASCADE, related_name="tecnologias")
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

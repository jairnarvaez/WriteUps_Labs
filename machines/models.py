from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Machine(models.Model):

    EMOJI_CHOICES = [
        ('🐧', '🐧'),
        ('📞', '📞'),
        ('🚀', '🚀'),
        ('🛸', '🛸'),
        ('🛰️', '🛰️'),
        ('👩‍🚀', '👩‍🚀'),
        ('👨‍🚀', '👨‍🚀'),
        ('🌌', '🌌'),
        ('🌠', '🌠'),
        ('🌑', '🌑'),
        ('🌒', '🌒'),
        ('🌓', '🌓'),
        ('🌔', '🌔'),
        ('🌕', '🌕'),
        ('🌖', '🌖'),
        ('🌗', '🌗'),
        ('🌘', '🌘'),
        ('🌙', '🌙'),
        ('☄️', '☄️'),
        ('🌍', '🌍'),
        ('🌎', '🌎'),
        ('🌏', '🌏'),
        ('🪐', '🪐'),
        ('🌞', '🌞'),
        ('🌟', '🌟'),
        ('✨', '✨'),
        ('🔭', '🔭'),
        ('📡', '📡'),
        ('🧪', '🧪'),
        ('🧬', '🧬'),
        ('🤖', '🤖'),
        ('🦾', '🦾'),
        ('🦿', '🦿'),
        ('🧠', '🧠'),
        ('💽', '💽'),
        ('💾', '💾'),
        ('📀', '📀'),
        ('🔋', '🔋'),
        ('🕹️', '🕹️'),
        ('💡', '💡'),
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    PLATFORM_CHOICES = [
        ('VulnHub', 'VulnHub'),
        ('HackThebox', 'HackThebox'),
        ('TryHackMe', 'TryHackMe'),
        ('OverTheWire', 'OverTheWire'),
    ]
    
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    emoji = models.CharField(max_length=10, choices=EMOJI_CHOICES, blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, blank=True)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True)
    summary = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='machines/covers/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Section(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=200, blank=True)  # Ej: "Enumeración", "Explotación"
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = (('machine', 'order'),)

    def __str__(self):
        return f"{self.machine.name} — {self.order}: {self.title}"


class Step(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='steps', null=True, blank=True)
    title = models.CharField(max_length=200)   # nombre del paso
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = (('section', 'order'),)

    def __str__(self):
        return f"{self.section.title} — {self.order}: {self.title}"


class StepBlock(models.Model):
    DESCRIPTION = 'description'
    CODE = 'code'
    IMAGE = 'image'
    MARKDOWN = 'markdown'
    BLOCK_TYPES = [
        (DESCRIPTION, 'Description'),
        (CODE, 'Code'),
        (IMAGE, 'Image'),
        (MARKDOWN, 'Markdown'),
    ]

    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='blocks')
    type = models.CharField(max_length=20, choices=BLOCK_TYPES)
    order = models.PositiveIntegerField(default=0)

    text = models.TextField(blank=True, help_text="Para description/markdown")
    code = models.TextField(blank=True, help_text="Para bloques de código")
    image = models.ImageField(upload_to='machines/steps/', blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['order']
        unique_together = (('step', 'order'),)

    def __str__(self):
        return f"{self.step} — {self.order} ({self.type})"

    def clean(self):
        # Limpiar/validar según el tipo
        if self.type == self.DESCRIPTION or self.type == self.MARKDOWN:
            if not self.text:
                raise ValidationError({'text': 'Este campo es obligatorio para Description o Markdown.'})
            if self.code or self.image:
                raise ValidationError('No puedes rellenar code o image para este tipo de bloque.')
        
        elif self.type == self.CODE:
            if not self.code:
                raise ValidationError({'code': 'Este campo es obligatorio para Code.'})
            if self.text or self.image:
                raise ValidationError('No puedes rellenar text o image para este tipo de bloque.')
        
        elif self.type == self.IMAGE:
            if not self.image:
                raise ValidationError({'image': 'Este campo es obligatorio para Image.'})
            if self.text or self.code:
                raise ValidationError('No puedes rellenar text o code para este tipo de bloque.')

    def render_markdown(self):
        if self.type == self.MARKDOWN:
            return markdown.markdown(self.text)
        return self.text

    def save(self, *args, **kwargs):
        self.clean()  # se asegura de validar antes de guardar
        super().save(*args, **kwargs)

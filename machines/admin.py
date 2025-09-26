from django.contrib import admin
from .models import Machine, Section, Step, StepBlock, Tag

class StepBlockInline(admin.StackedInline):
    model = StepBlock
    extra = 1
    fields = ('order', 'type', 'text', 'code', 'image', 'caption')

class StepInline(admin.StackedInline):
    model = Step
    extra = 1
    fields = ('order', 'title')
    inlines = [StepBlockInline]

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1
    fields = ('order', 'title')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    list_display = ('name', 'difficulty', 'created_at')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [StepInline]
    list_display = ('machine', 'order', 'title')

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    inlines = [StepBlockInline]
    list_display = ('section', 'order', 'title')

admin.site.register(Tag)

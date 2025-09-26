from django.contrib import admin
from .models import ContactMessage
from .models import (
    ContactPage, PersonalInfo, PersonalList, PersonalListItem,
    Objective, ObjectiveSubsection, PersonalProject, ProjectTechnology
)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
    list_filter = ("created_at",)

class PersonalListItemInline(admin.TabularInline):
    model = PersonalListItem
    extra = 1

class PersonalListInline(admin.TabularInline):
    model = PersonalList
    extra = 1

class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1

class PersonalInfoAdmin(admin.ModelAdmin):
    inlines = [PersonalListInline]

class PersonalListAdmin(admin.ModelAdmin):
    inlines = [PersonalListItemInline]

class PersonalProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectTechnologyInline]

admin.site.register(ContactPage)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(PersonalList, PersonalListAdmin)
admin.site.register(Objective)
admin.site.register(ObjectiveSubsection)
admin.site.register(PersonalProject, PersonalProjectAdmin)

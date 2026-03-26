from django.contrib import admin
from .models import ContactMessage, Project, Skill, Certification


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    ordering = ['-created_at']

    fieldsets = (
        ('Sender Info', {'fields': ('name', 'email')}),
        ('Message', {'fields': ('subject', 'message')}),
        ('Meta', {'fields': ('is_read', 'created_at')}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'emoji', 'order', 'is_featured']
    list_editable = ['order', 'is_featured']
    search_fields = ['title', 'description']
    list_filter = ['is_featured', 'project_type']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'icon', 'order']
    list_editable = ['order']
    search_fields = ['title', 'issuer']

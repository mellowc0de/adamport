from django.contrib import admin
from .models import workExperience, Certificates
from tinymce.widgets import TinyMCE
from django.db import models


class workExperienceAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Position/Location/Company", {"fields": ["position", "location", "company"]}),
        ("Content", {"fields": ["description"]}),
        ("Utilities", {"fields": ["uniqueId", "slug","start_date", "current", "end_date", "last_updated"]})
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class CertificatesAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Certification Details", {"fields": ["course_name", "course_code", "issued_by", "date_issued", "cert_id", "valid_cert_link"]}),
        ("Content", {"fields": ["image","description"]}),
        ("Utilities", {"fields": ["uniqueId", "slug", "last_updated"]})
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

# Register your models here.
admin.site.register(workExperience, workExperienceAdmin)
admin.site.register(Certificates, CertificatesAdmin)


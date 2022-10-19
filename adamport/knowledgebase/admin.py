from django.contrib import admin
from .models import TutorialCategory, TutorialSeries, Tutorial, Documents
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


class DocumentsAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Title/Published", {'fields': ["document_title", "document_published"]}),
    ("Content/Article", {'fields': ["document_content","document_article"]}),
    ("Utilies", {'fields': []}),
    ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Documents,DocumentsAdmin)
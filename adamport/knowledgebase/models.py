from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
        
        
# Tutorial Models
# Parent Class - TutorialCategory
class TutorialCategory(models.Model):
    
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

# Tutorial Models
# Child Class - TutorialSeries
class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

# Tutorial Models
# Child Sub-Class - TutorialSeries
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)
    
    def __str__(self):
        return self.tutorial_title
        
# Documents Model
# 
class Documents(models.Model):
    document_title = models.CharField(max_length=200)
    document_content = models.TextField()
    document_article = RichTextField()
    document_published = models.DateTimeField('date published')
    
    
    def __str__(self):
        return self.document_title
    
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Documents"
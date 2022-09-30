from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User


class Profile(models.Model):
    fname = models.CharField(null=True, blank=True, max_length=60)
    mname = models.CharField(null=True, blank=True, max_length=20)
    lname = models.CharField(null=True, blank=True, max_length=60)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {} {}'.format(self.fname, self.lname, self.username)

class workExperience(models.Model):
    position = models.CharField(null=True, blank=True, max_length=60)
    location = models.CharField(null=True, blank=True, max_length=60)
    company = models.CharField(null=True, blank=True, max_length=60)
    start_date = models.DateField()
    current = models.BooleanField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Work Experience"
    
    def __str__(self):
        return '{} {} {}'.format(self.position, self.company, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse('work_experience_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.end_date is None:
            self.end_date = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.company, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(workExperience, self).save(*args, **kwargs)
        
class Certificates(models.Model):
    course_name = models.CharField(null=True, blank=True, max_length=60)
    course_code = models.CharField(null=True, blank=True, max_length=60)
    issued_by = models.CharField(null=True, blank=True, max_length=60)
    date_issued = models.DateField()
    cert_id = models.CharField(null=True, blank=True, max_length=60)
    valid_cert_link = models.URLField()
    image = models.ImageField(upload_to='uploads/certs')
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Certificates"
    
    def __str__(self):
        return '{} {} {}'.format(self.course_code, self.cert_id, self.uniqueId)
        
    def get_absolute_url(self):
        return reverse('certificate_detail', kwargs={'slug': self.slug})
        
    def save(self, *args, **kwargs):
      if self.last_updated is None:
        self.last_updated = timezone.localtime(timezone.now())
      if self.uniqueId is None:
        self.uniqueId = str(uuid4()).split('-')[4]
        self.slug = slugify('{} {}'.format(self.cert_id, self.uniqueId))
      self.last_updated = timezone.localtime(timezone.now())
      super(Certificates, self).save(*args, **kwargs)
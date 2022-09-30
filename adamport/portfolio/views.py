from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Profile, workExperience, Certificates


class pIndex(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all()
        experience = workExperience.objects.order_by('-start_date')
        certs = Certificates.objects.order_by('-date_issued')
        
        context = {
            'profile': profile,
            'experience': experience,
            'certs': certs,
        }
        
        return render(request, 'portfolio/pIndex.html', context)
        
class workExperienceDetail(View):
    def get(self, request, *args, **kwargs):
        experience = workExperience.objects.order_by('start_date')
        
        context = {
            'experience': experience,
        }
        
        return render(request, 'portfolio/work_experience_detail.html', context)

class certificatesDetail(View):
   def get(self, request, *args, **kwargs):
       certs = Certificates.objects.order_by('-date_issued')
       
       context = {
           'certs': certs,
       }
       
       return render(request, 'portfolio/certificates_detail.html', context)

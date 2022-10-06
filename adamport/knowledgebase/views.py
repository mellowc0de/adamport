from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import TutorialCategory, TutorialSeries, Tutorial, Documents


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        
        series_urls ={}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug
            
        return render(request=request,
                      template_name='knowledgebase/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})
    
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)
        return render(request = request,
                      template_name='knowledgebase/tutorial.html',
                      context = {"tutorial": this_tutorial,
                               "sidebar": tutorials_from_series,
                               "this_tut_idx": this_tutorial_idx})
    
    return HttpResponse(f"{single_slug} does not correspond to anything.")

def kbIndex(request):
    return render(request=request,
        template_name="knowledgebase/kb_index.html",
        context={"categories": TutorialCategory.objects.all,
                 "documents":Documents.objects.all,
                })

def categories(request):
    return render(request=request,
        template_name="knowledgebase/categories.html",
        context={"categories": TutorialCategory.objects.all})
    

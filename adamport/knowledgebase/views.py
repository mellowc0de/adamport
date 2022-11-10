from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import TutorialCategory, TutorialSeries, Tutorial, Documents
from .forms import documentsForm

# View for single slug urls
# Slug used for series_urls and tutorials
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

# KB Index View
# context - categories, documents
#def kbIndex(request):
#    return render(request=request,
#        template_name="knowledgebase/kb_index.html",
#        context={"categories": TutorialCategory.objects.all,
#                 "documents":Documents.objects.all,
#                })
class kbIndex(LoginRequiredMixin, View):
    """kbIndex view constructs the views for the index page of KB. POST and GET are defined here."""
    def get(self, request, *args, **kwargs):
        categories = TutorialCategory.objects.all
        documents = Documents.objects.all

        form = documentsForm()
        
        context = {
            'categories': categories,
            'documents': documents,
            'form': form,
        }
        
        return render(request, 'knowledgebase/kb_index.html', context)
    
    def post(self, request, *args, **kwargs):
        categories = TutorialCategory.objects.all
        documents = Documents.objects.all

        form = documentsForm(request.POST)
        
        if form.is_valid():
            new_document = form.save(commit=False)
            #new_document.creator = request.user
            new_document.save()
            
        context = {
            'categories': categories,
            'documents': documents,
            'form': form,
        }
        
        return render(request, 'knowledgebase/kb_index.html', context)



# Categories View
# context - categories
def categories(request):
    return render(request=request,
        template_name="knowledgebase/categories.html",
        context={"categories": TutorialCategory.objects.all})
    
# Document Detail View
# context - document, pk
class document_detail_view(View):
    def get(self, request, *args, **kwargs):
        document = get_object_or_404(Documents, pk=kwargs['pk'])
        context = {
            'document': document
        }
        return render(request, 'knowledgebase/document_detail.html', context)



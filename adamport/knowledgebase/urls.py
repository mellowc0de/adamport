from django.urls import path
from . import views
#from knowledgebase.views import DocumentsDetailView
#from knowledgebase.views import document_detail_view

urlpatterns = [
    path('', views.kbIndex.as_view(), name='kb_index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<single_slug>', views.single_slug, name="single_slug"),
    path('docs/<int:pk>/', views.document_detail_view.as_view(), name='document-detail'),
    #path('docs/<int:pk>/', views.DocumentsDetailView.as_view(), name='document-detail'),
]

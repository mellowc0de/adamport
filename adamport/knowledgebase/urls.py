from django.urls import path
from . import views

urlpatterns = [
    path('', views.kbIndex, name='kb_index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<single_slug>', views.single_slug, name="single_slug"),
]

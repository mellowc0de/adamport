from django import forms
from .models import Documents
from ckeditor.widgets import CKEditorWidget
#from django.contrib.auth.models import User

class documentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['document_title','document_content','document_article','document_published']
        
        widgets = {
            'document_title': forms.TextInput(attrs={'class': 'form-control w3-input w3-padding', 'placeholder': 'Document Title'}), 
            'document_content': forms.Textarea(attrs={'class': 'form-control w3-input w3-padding', 'placeholder': 'Content Summary'}), 
            'document_article': forms.CharField(widget=CKEditorWidget()),
            'document_published': forms.DateTimeInput(attrs={'class': 'form-control'}), 
        }
        
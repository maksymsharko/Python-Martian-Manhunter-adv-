from django import forms

from src.apps.newsletter.models import NewsLetter


class NewsLetterModelForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
        labels = {'Email': ''}
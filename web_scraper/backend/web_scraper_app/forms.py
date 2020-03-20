from django import forms
from .models import WebPage


class WebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage()
        fields = ['url', ]
        # fields = '__all__'

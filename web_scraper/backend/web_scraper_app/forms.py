from django import forms
from .models import WebPage


class WebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage()
        fields = ['url', ]
        model.gettext()
        # fields = '__all__'

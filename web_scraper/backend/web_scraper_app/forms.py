from django import forms


class WebPageForm(forms.Form):
    url = forms.URLField()

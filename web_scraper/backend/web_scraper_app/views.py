from django.shortcuts import render

from .forms import WebPageForm
from .models import *


# def home(request):
#     home_dict = {'index_insert': "Hello, please enter address URL and click Submit"}
#     return render(request, 'web_scraper/--home.html', context=home_dict)


# def help(request):
#     help_dict = {'help_insert': "Sorry, i Can't help you :("}
#     return render(request, 'web_scraper/help.html', context=help_dict)


def list_url(request):
    page_list = WebPage.objects.order_by("url")
    list_dict = {"page_list_insert": page_list}
    return render(request, 'list_url.html', context=list_dict)

def list_text(request):
    text_list = Texts.objects.order_by("head")
    list_dict = {"text_list_insert": text_list}
    return render(request, 'list_text.html', context=list_dict)

def home(request):
    form = WebPageForm()
    home_dict = {"insert_form": form,
                   "welcome_form": "Hello, please enter address URL and click Submit"}

    if request.method == "POST":
        form = WebPageForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # print("VALIDATION SUCCESS")
            print("URL: " + form.cleaned_data['url'])
            # print("Nazwisko: " + form.cleaned_data['last_name'])
            # print("Numer telefonu: " +form.cleaned_data['phone_number'])
            # print("Adres e-mail: " + form.cleaned_data['email'])
            # print("VERIFY EMAIL: " + form.cleaned_data['verify_email'])
            return home(request)

        else:
            print('ERROR FORM INVALID / Email, not unique /')

    return render(request, 'web_scraper/home.html', context=home_dict)

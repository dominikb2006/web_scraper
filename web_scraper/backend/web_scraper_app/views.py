from django.shortcuts import render

from .forms import WebPageForm
from .models import *
from .backend import *


def list_url(request):
    page_list = WebPage.objects.order_by("url")
    list_dict = {"page_list_insert": page_list}
    return render(request, 'list_url.html', context=list_dict)


def list_text(request):
    text_list = WebPage.objects.order_by("url")
    list_dict = {"text_list_insert": text_list}
    return render(request, 'list_text.html', context=list_dict)


def list_images(request):
    # text_list = WebPage.objects.order_by("url")
    list_dict = {}
    return render(request, 'list_images.html', context=list_dict)

def results(request):  # ,url):
    form = WebPageForm()
    WebPage.gettext()

    result_dict = {"result_text": WebPageForm.text}
    return render(request, 'results.html', context=result_dict)


def home(request):
    model = WebPage()
    # home_dict = {"insert_form": form,
    #                "welcome_form": "Hello, please enter address URL and click Submit"}

    if request.method == "POST":
        url = request.POST.get('url')
        model.url = url
        model.text = urlIntoText(url)
        model.save()
        return render(request, 'home.html')
        # form = WebPageForm(request.POST)
        #
        # if form.is_valid():
        #     # q=form.Meta.model
        #     # q.gettext()
        #     form.save(commit=True)
        #     # print("VALIDATION SUCCESS")
        #     print("URL: " + form.cleaned_data['url'])
        #     # print("Nazwisko: " + form.cleaned_data['last_name'])
        #     # print("Numer telefonu: " +form.cleaned_data['phone_number'])
        #     # print("Adres e-mail: " + form.cleaned_data['email'])
        #     # print("VERIFY EMAIL: " + form.cleaned_data['verify_email'])
        #     return results(request)#,form.cleaned_data['url'])
        #
        # else:
        #     print('ERROR FORM INVALID / Email, not unique /')

    return render(request, 'home.html')  # , context=home_dict)

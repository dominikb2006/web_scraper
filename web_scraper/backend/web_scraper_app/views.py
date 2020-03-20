from django.shortcuts import render

from .forms import WebPageForm
from .models import *
from .backend import *


def list_text(request):
    text_list = WebPage.objects.order_by("url")
    list_dict = {"text_list_insert": text_list,
                 "header": "List of Texts from Websites"}
    return render(request, 'list_text.html', context=list_dict)


def list_images(request):
    # text_list = WebPage.objects.order_by("url")
    list_dict = {}
    return render(request, 'list_images.html', context=list_dict)


def results(request):  # ,url):
    form = WebPageForm()

    result_dict = {"result_text": WebPageForm.text}
    return render(request, 'results.html', context=result_dict)


def home(request):
    wrong_url_form = ''
    home_dict = {"wrong_url_form": wrong_url_form,
                 "welcome_form": "Hello, please enter address URL and click Submit"}

    if request.method == "POST":
        url = request.POST.get('url')
        if is_valid(url):
            modelWP = WebPage(url=url, text=urlIntoText(url))
            modelWP.save()

            images_url = get_all_images(url)
            for image_url in images_url:
                
                modelI = Images(id=None, image_url=image_url, url=modelWP)
                modelI.save()

            return render(request, 'home.html', context=home_dict)
        else:
            wrong_url_form = "Wrong URL"
            home_dict = {"wrong_url_form": wrong_url_form,
                         "welcome_form": "Hello, please enter address URL and click Submit"}
            return render(request, 'home.html', context=home_dict)
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

    return render(request, 'home.html', context=home_dict)

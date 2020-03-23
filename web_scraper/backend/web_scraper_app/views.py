from shutil import make_archive
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render
import csv
from django.utils.encoding import smart_str
from .models import *
from .backend import *


def list_texts(request):
    text_list = WebPage.objects.order_by("-id") #[:1]
    list_dict = {"text_list_insert": text_list,
                 "header": "List of Texts from Websites"}
    return render(request, 'list_texts.html', context=list_dict)


def list_images(request):
    image_list = Image.objects.order_by("-id")
    list_dict = {"image_list_insert": image_list,
                 "header": "List of Images from Websites"}
    return render(request, 'list_images.html', context=list_dict)


def home(request):
    wrong_url_form = 'Wrong URL'
    home_dict = {"wrong_url_form": "",
                 "welcome_form": "Hello, please enter address URL and click Submit"}

    if request.method == "POST":
        url = request.POST.get('url')
        if is_valid(url):

            WebPage = WebPage(url=url,
                              text=url_into_text(url))
            WebPage.save()
            images_url = get_all_images(url)

            for image_url in images_url:
                image = Image(image_url=image_url,
                              url=WebPage)
                image.set_name()
                image.set_local_url()
                try:
                    image.save_photo()
                    image.save()
                except:
                    None #do nothing, u cant save this image

        else:
            home_dict["wrong_url_form"] = wrong_url_form

    return render(request, 'home.html', context=home_dict)


def get_images(request):
    file_name = "Images"
    files_path = settings.MEDIA_ROOT
    path_to_zip = make_archive(files_path, "zip", files_path)
    response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
        filename=file_name.replace(" ", "_")
    )
    return response


def get_texts(request):
    response = HttpResponse(content_type='text/csv')
    # decide the file name
    response['Content-Disposition'] = 'attachment; filename="Texts.csv"'

    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    # headers
    writer.writerow([
        smart_str(u"Website URL"),
        smart_str(u"Website text")
    ])
    # get data from database
    pages = WebPage.objects.order_by("-id")
    for page in pages:
        writer.writerow([
            smart_str(page.url),
            smart_str(page.text)
        ])
    return response

from shutil import make_archive
from wsgiref.util import FileWrapper
from django.http import HttpResponse

from django.shortcuts import render

from .forms import *
from .models import *
from .backend import *


def list_text(request):
    text_list = WebPage.objects.order_by("-id")
    list_dict = {"text_list_insert": text_list,
                 "header": "List of Texts from Websites"}
    return render(request, 'list_text.html', context=list_dict)


def list_images(request):
    image_list = Image.objects.order_by("-id")
    list_dict = {"image_list_insert": image_list}
    return render(request, 'list_images.html', context=list_dict)

def home(request):
    wrong_url_form = 'Wrong URL'
    home_dict = {"wrong_url_form": '',
                 "welcome_form": "Hello, please enter address URL and click Submit"}

    if request.method == "POST":
        url = request.POST.get('url')
        if is_valid(url):

            modelWP = WebPage(url=url, text=urlIntoText(url))
            modelWP.save()

            images_url = get_all_images(url)
            for image_url in images_url:
                modelI = Image(image_url=image_url,
                               url=modelWP,
                               name=image_url.split("/")[-1])
                modelI.setLocalURL()
                modelI.cache()
                modelI.save()
                print(modelI)

        else:
            home_dict["wrong_url_form"] = wrong_url_form

    return render(request, 'home.html', context=home_dict)


# def download(request, file_name):
#     file_path = settings.MEDIA_ROOT + '/' + file_name
#     file_wrapper = FileWrapper(file(file_path, 'rb'))
#     file_mimetype = mimetypes.guess_type(file_path)
#     response = HttpResponse(file_wrapper, content_type=file_mimetype)
#     response['X-Sendfile'] = file_path
#     response['Content-Length'] = os.stat(file_path).st_size
#     response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name)
#     return response


def getImages(request):
    file_name = "Images"
    """
    A django view to zip files in directory and send it as downloadable response to the browser.
    Args:
      @request: Django request object
      @file_name: Name of the directory to be zipped
    Returns:
      A downloadable Http response
    """
    files_path = settings.MEDIA_ROOT
    path_to_zip = make_archive(files_path, "zip", files_path)
    response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
        filename=file_name.replace(" ", "_")
    )
    return response
import csv
from django.utils.encoding import smart_str

def getTexts(request):
    response = HttpResponse(content_type='text/csv')
    # decide the file name
    response['Content-Disposition'] = 'attachment; filename="Texts.csv"'

    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    # write the headers
    writer.writerow([
        smart_str(u"Website URL"),
        smart_str(u"Website text")
    ])
    # get data from database or from text file....
    pages = WebPage.objects.order_by("-id")
    for page in pages:
        writer.writerow([
            smart_str(page.url),
            smart_str(page.text)
        ])
    return response
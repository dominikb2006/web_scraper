from django.shortcuts import render

from .forms import NewUserForm
from .models import User


def home(request):
    index_dict = {'index_insert': "Yup, Its index"}
    return render(request, 'web_scraper/home.html', context=index_dict)


def help(request):
    help_dict = {'help_insert': "Sorry, i Can't help you :("}
    return render(request, 'web_scraper/help.html', context=help_dict)


def signin(request):
    webpages_list = User.objects.order_by("FirstName")
    users_dict = {"users_list_insert": webpages_list,
                  'users_insert': "THERE IS A LIST! LIST I SAID!"}
    return render(request, 'web_scraper/signin.html', context=users_dict)

def signup(request):
    form = NewUserForm()
    signup_dict = {"signup_form": form}

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("VALIDATION SUCCESS")
            print("Imię: " + form.cleaned_data['first_name'])
            print("Nazwisko: " + form.cleaned_data['last_name'])
            print("Numer telefonu: " +form.cleaned_data['phone_number'])
            print("Adres e-mail: " + form.cleaned_data['email'])
            # print("VERIFY EMAIL: " + form.cleaned_data['verify_email'])
            return home(request)

        else:
            print('ERROR FORM INVALID / Email, not unique /')

    return render(request, 'web_scraper/signup.html', context=signup_dict)

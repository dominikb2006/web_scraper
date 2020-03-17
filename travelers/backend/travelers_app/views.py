from django.shortcuts import render

from .forms import NewUserForm
from .models import User


def home(request):
    index_dict = {'index_insert': "Yup, Its index"}
    return render(request, 'travelers/home.html', context=index_dict)


def help(request):
    help_dict = {'help_insert': "Sorry, i Can't help you :("}
    return render(request, 'travelers/help.html', context=help_dict)


def signin(request):
    webpages_list = User.objects.order_by("FirstName")
    users_dict = {"users_list_insert": webpages_list,
                  'users_insert': "THERE IS A LIST! LIST I SAID!"}
    return render(request, 'travelers/signin.html', context=users_dict)


def signup(request):
    form = NewUserForm()

    if request.method == "POST":
        signup_form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('Błędne wartości')

    return render(request, 'travelers/users.html', {'signup_form': form})

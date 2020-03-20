"""web_scraper_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path
from web_scraper_app import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list_url/', views.list_url, name="list_url"),
    path('list_text/', views.list_text, name="list_text"),
    path('list_images/', views.list_images, name="list_images"),
    path('results/', views.results, name="results"),
    # path('signin/', views.signin, name='signin'),
    # path('help/', views.help, name='help'),
    # path('web_scraper/', include('web_scraper_app.urls')),
]

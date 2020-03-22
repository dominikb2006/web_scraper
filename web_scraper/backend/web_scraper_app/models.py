from django.db import models
from django.core.files import File
import urllib.request
import os
from django.conf import settings


class WebPage(models.Model):
    url = models.URLField(max_length=5000)  # unique=True,
    text = models.TextField(default='')

    def __str__(self):
        return str(self.url)


class Image(models.Model):
    url = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    image_url = models.URLField(default='', max_length=5000)  # unique=True,
    local_image_url = models.CharField(default='', max_length=5000)
    name = models.CharField(max_length=1000, default='')
    photo = models.ImageField(blank=True, default=None)

    def __str__(self):
        return str(self.image_url)

    def setLocalURL(self):
        self.local_image_url = str(settings.MEDIA_URL + self.name)

    def cache(self):
        """Store image locally if we have a URL"""

        if self.image_url and not self.photo:
            result = urllib.request.urlretrieve(self.image_url)
            self.photo.save(
                os.path.basename(self.name),
                File(open(result[0], 'rb'))
            )
            self.save()

from django.db import models


class WebPage(models.Model):
    url = models.URLField(max_length=5000)  # unique=True,
    text = models.TextField(default='')

    def __str__(self):
        return str(self.url)


class Images(models.Model):
    url = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    image_url = models.URLField(default='', max_length=5000)  # unique=True,
    photo = models.ImageField()

    def __str__(self):
        return str(self.image_url)

from django.db import models


class WebPage(models.Model):
    url = models.TextField(unique=True)

    def __str__(self):
        return str(self.url)


class Texts(models.Model):
    source = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    head = models.TextField()
    text = models.TextField()

    def __str__(self):
        return str(self.head)


class Images(models.Model):
    source = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    photo = models.CharField(max_length=10)  # ImageField()

from django.db import models


class WebPage(models.Model):
    url = models.TextField(unique=True)
    text = models.TextField(default='')

    def __str__(self):
        return str(self.url)

    # def gettext(self, **kwargs):
    #     self.text = str(self.url)+"1111"
    #     super(WebPage, self).save(**kwargs)
    # def __init__(self):
    #     self.text = self.url + "1111"
    def gettext(self):
        self.text = str(self.url) + "1111"


class Images(models.Model):
    source = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    photo = models.CharField(max_length=10)  # ImageField()

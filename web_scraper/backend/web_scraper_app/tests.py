from django.test import TestCase, Client
from django.urls import reverse
from .models import Image, WebPage

# view test
client = Client()


class HomeViewTest(TestCase):
    def test_home(self):
        url = 'home'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["welcome_form"], ['Hello, please enter address URL and click Submit'][0])
        self.assertQuerysetEqual(response.context['wrong_url_form'], [])
        self.assertTemplateUsed(response, 'home.html')

    def test_list_texts(self):
        url = 'list_texts'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["header"], ['List of Texts from Websites'][0])
        self.assertQuerysetEqual(response.context["text_list_insert"], [])
        self.assertTemplateUsed(response, 'list_texts.html')

    def test_list_images(self):
        url = 'list_images'
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["header"], ['List of Images from Websites'][0])
        self.assertQuerysetEqual(response.context["image_list_insert"], [])
        self.assertTemplateUsed(response, 'list_images.html')

    def setUp(self):
        self.webpage = WebPage(url='https://testWebSite.com', text="TESTESTESTESTEST")

    def test_home_setwebpage(self):
        url = 'home'
        data = {'https://testWebSite.com': "TESTESTESTESTEST"}
        response = self.client.post(reverse(url), data)
        self.assertEqual(response.status_code, 200)


# models test
class ImageModelTests(TestCase):

    def setUp(self):
        self.webpage = WebPage(url="https://testWebSite.com", text="TESTESTESTESTEST")
        self.image = Image(url=self.webpage,
                           image_url="https://testImage.com/testname1.jpg")

    # def tearDown(self):
    #     self.webpage.delete()
    #     self.image.delete()

    def test_set_name(self):
        self.image.set_name()
        response = self.image.name
        self.assertEqual(response, 'testname1.jpg')

    def test_set_local_url(self):
        self.image.set_name()
        self.image.set_local_url()
        response = self.image.local_image_url
        self.assertEqual(response, '/media/testname1.jpg')

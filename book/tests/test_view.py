from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from book import views

class TestDashboardPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("book:dashboard")

        self.response = self.client.get(self.url)

    def test_page_status(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):

        self.assertTemplateUsed(self.response, 'book/dashboard.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.DashboardView)


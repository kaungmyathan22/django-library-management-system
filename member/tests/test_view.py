from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth import login
from model_mommy import mommy
from member import views

class TestMemberListPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("member:member-list")

        self.response = self.client.get(self.url)

    def login_user(self):
    
        self.user = User.objects.create_user(
            username="kaung", password='password')

        self.client.post(reverse('login'), data={
            'username': 'kaung',
            'password': 'password'
        })

        self.response = self.client.get(self.url)

    def test_page_status_with_login(self):

        self.login_user()

        self.assertEqual(self.response.status_code, 200)

    def test_page_status_without_login(self):
    
        self.assertEqual(self.response.status_code, 302)

    def test_template_used(self):

        self.login_user()

        self.assertTemplateUsed(self.response, 'member/member_list.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.MemberListView)


class TestMemberCreatePage(TestCase):

    def login_user(self):
        
        self.user = User.objects.create_user(
            username="kaung", password='password')

        self.client.post(reverse('login'), data={
            'username': 'kaung',
            'password': 'password'
        })

        self.response = self.client.get(self.url)


    def setUp(self):

        self.client = Client()

        self.url = reverse("member:member-create")

        self.response = self.client.get(self.url)

    def test_page_status(self):

        self.login_user()

        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):

        self.login_user()

        self.assertTemplateUsed(self.response, 'member/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.MemberCreateView)

    def test_page_status_with_login(self):
    
        self.login_user()

        self.assertEqual(self.response.status_code, 200)

    def test_page_status_without_login(self):
    
        self.assertEqual(self.response.status_code, 302)

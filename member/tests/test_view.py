from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth import login
from model_mommy import mommy
from django.utils import timezone
from member import views
from member.models import Member

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

        self.model = Member

    def test_page_status(self):

        self.login_user()

        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):

        self.login_user()

        self.assertTemplateUsed(self.response, 'member/form.html')

    def test_create_member(self):

        self.login_user()

        data = {
            'first_name':"Km",
            'last_name':"Km",
            'email':'hello@gmail.com',
            'born': '03/08/2019 14:00',
            'roll_no':'4cs-1'
        }

        self.response = self.client.post(self.url, data)

        self.assertEqual(self.response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.MemberCreateView)

    def test_page_status_with_login(self):
    
        self.login_user()

        self.assertEqual(self.response.status_code, 200)

    def test_page_status_without_login(self):
    
        self.assertEqual(self.response.status_code, 302)

class TestMemberDeleteView(TestCase):
    
    def setUp(self):

        self.client = Client()

        self.model = Member

        self.instance = mommy.make(self.model)

        self.url = reverse('member:member-delete',
                           kwargs={'pk': self.instance.pk})

        self.view = views.member_delete_view

    def login_user(self):

        self.user = User.objects.create_user(
            username="kaung", password='password')

        self.client.post(reverse('login'), data={
            'username': 'kaung',
            'password': 'password'
        })

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, self.view)

    def test_book_delete_view(self):

        self.login_user()

        self.response = self.client.post(self.url)

        self.assertEqual(self.response.status_code, 200)

        self.assertFalse(self.model.objects.exists())


class TestMemberUpdateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Member

        self.instance = mommy.make(self.model)

        self.url = reverse('member:member-update',
                           kwargs={'slug': self.instance.slug})

        self.view = views.MemberUpdateView

    def login_user(self):

        self.user = User.objects.create_user(
            username="kaung", password='password')

        self.client.post(reverse('login'), data={
            'username': 'kaung',
            'password': 'password'
        })

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_shelf_update_view(self):

        self.login_user()

        data = {
            'first_name': "Km",
            'last_name': "Km",
            'email': 'hello@gmail.com',
            'born': '03/08/2019 14:00',
            'roll_no': '4cs-1'
        }

        response = self.client.post(reverse("member:member-create"), data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

        obj = self.model.objects.last()

        data['first_name'] = 'updated first name'

        response = self.client.post(
            reverse('member:member-update', kwargs={'slug': obj.slug}), data)

        expected = "updated first name"

        actual = self.model.objects.last().first_name

        self.assertEqual(actual, expected)
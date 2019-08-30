from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from model_mommy import mommy
from issue import views
from issue.models import Issue
from issue import forms

class TestIssueCreateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Issue

        self.creation_form = forms.IssueAddForm

        self.url = reverse("issue:issue-create")

        self.view = views.IssuedBookCreateView

        self.response = self.client.get(self.url)

    def test_page_status_without_login(self):

        actual = self.response.status_code

        expected = 302

        self.assertEqual(actual, expected)

    def login_user(self):

        self.user = User.objects.create_user(
            username="kaung", password='password')

        self.client.post(reverse('login'), data={
            'username': 'kaung',
            'password': 'password'
        })

        self.response = self.client.get(self.url)

    def test_page_status_after_login(self):

        self.login_user()

        actual = self.response.status_code

        expected = 200

        self.assertEqual(actual, expected)

    def test_template_used(self):

        self.login_user()

        self.assertTemplateUsed(self.response, 'issue/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)  # cbv

    def test_issue_create_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_create_issue_view(self):

        self.login_user()

        book = mommy.make("Book")
        member = mommy.make("member")

        data = {
            'book': book.pk,
            'member': member.pk,
            'date': '03/08/2019 14:00'
        }

        self.response = self.client.post(self.url, data)


        self.assertEqual(self.response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

    def test_form_inputs(self):

        self.login_user()

        self.assertContains(self.response, '<input', 2)
        
        self.assertContains(self.response, '<select', 2)

        self.assertContains(self.response, 'type="text"', 1)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="submit"', 1)

        self.assertContains(self.response, 'type="reset"', 1)


class TestIssueListView(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("issue:issue-list")

        self.response = self.client.get(self.url)

    def login_user(self):

        self.user = User.objects.create_user(
            username="kaung", password='password')

        self.client.post(reverse('login'), data={
            'username': 'kaung',
            'password': 'password'
        })

        self.response = self.client.get(self.url)

    def test_page_status_without_login(self):

        actual = self.response.status_code

        expected = 302

        self.assertEqual(actual, expected)

    def test_page_status_after_login(self):

        self.login_user()

        actual = self.response.status_code

        expected = 200

        self.assertEqual(actual, expected)

    def test_template_used(self):

        self.login_user()

        self.assertTemplateUsed(self.response, 'issue/issue_list.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.IssuedBookListView)

        # self.assertEqual(view_fun.func, views.@todo) # fbv


class TestIssueDeleteView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Issue

        self.instance = mommy.make(self.model)

        self.url = reverse('issue:issue-delete',
                           kwargs={'pk': self.instance.pk})

        self.view = views.issue_delete_view

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


class TestIssueUpdateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Issue

        self.instance = mommy.make(self.model)

        self.url = reverse('issue:issue-update', kwargs={'pk':self.instance.pk})

        self.view = views.issue_update_view

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

    def test_issue_update_view(self):

        self.login_user()

        book = mommy.make("Book")
        member = mommy.make("member")

        data = {
            'book': book.pk,
            'member': member.pk,
            'date': '03/08/2019 14:00'
        }

        response = self.client.post(reverse("issue:issue-create"), data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

        obj = self.model.objects.last()

        new_member = mommy.make("Member")

        data['member'] = new_member.pk

        response = self.client.post(
            reverse('issue:issue-update', kwargs={'pk': obj.pk}), data)

        expected = new_member.pk

        actual = self.model.objects.last().member.pk

        self.assertEqual(actual, expected)

class TestIssueRecieveReturnView(TestCase):
    
    def setUp(self):

        self.client = Client()

        self.model = Issue

        self.instance = mommy.make(self.model)

        self.url = reverse('issue:issue-return', kwargs={'pk':self.instance.pk})

        self.view = views.recieve_issue_book_view

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

    def test_shelf_update_view(self):

        self.login_user()

        response = self.client.get(self.url)

        obj = Issue.objects.get(pk=self.instance.pk)

        self.assertEqual(response.status_code, 200)

        self.assertIsNotNone(obj.return_date)
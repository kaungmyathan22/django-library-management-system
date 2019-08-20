from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from accounts.forms import SignUpForm
from accounts import views

class TestLoginView(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("login")

        self.response = self.client.get(self.url)

    def test_login_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_login_view(self):

        view = resolve(self.url)

        self.assertEqual(view.func.view_class, LoginView)

    def test_login_form(self):

        form = self.response.context.get('form')

        self.assertIsInstance(form, AuthenticationForm)

    def test_form_inputs(self):

        self.assertContains(self.response, '<input', 4)

        self.assertContains(self.response, 'type="text"', 1)

        self.assertContains(self.response, 'type="password"', 1)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="submit"', 1)


class SignUpView(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("register")

        self.response = self.client.get(self.url)

    def test_signup_page_status_code(self):

        self.assertEqual(self.response.status_code, 200)

    def test_singup_form(self):

        form = self.response.context.get("form")

        self.assertIsInstance(form, SignUpForm)

    def test_csrf(self):

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_template_use(self):

        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signup_view(self):

        view = resolve(self.url)

        self.assertEqual(view.func.view_class, views.SignUpView)

    def test_signup_form(self):

        form = self.response.context.get('form')

        self.assertIsInstance(form, SignUpForm)

    def test_create_user_view(self):

        data = {
            'username': "arkar",
            'email': 'arkar@gmail.com',
            'password1': 'kaungmyathan11209!@',
            'password2': 'kaungmyathan11209!@'
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(User.objects.exists())

    def test_form_inputs(self):

        self.assertContains(self.response, '<input', 6)

        self.assertContains(self.response, 'type="text"', 1)

        self.assertContains(self.response, 'type="password"', 2)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="email"', 1)

        self.assertContains(self.response, 'type="submit"', 1)


class PasswordChangeTestCase(TestCase):
    def setUp(self, data={}):
        self.user = User.objects.create_user(
            username='john', email='john@doe.com', password='old_password')
        self.url = reverse('password_change')
        self.client.login(username='john', password='old_password')
        self.response = self.client.post(self.url, data)


class SuccessfulPasswordChangeTests(PasswordChangeTestCase):
    def setUp(self):
        super().setUp({
            'old_password': 'old_password',
            'new_password1': 'new_password',
            'new_password2': 'new_password',
        })

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        self.assertRedirects(self.response, reverse('password_change_done'))

    def test_password_changed(self):
        '''
        refresh the user instance from database to get the new password
        hash updated by the change password view.
        '''
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('new_password'))



class InvalidPasswordChangeTests(PasswordChangeTestCase):
    def test_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_didnt_change_password(self):
        '''
        refresh the user instance from the database to make
        sure we have the latest data.
        '''
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('old_password'))

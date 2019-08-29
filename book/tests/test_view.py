from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth import login
from model_mommy import mommy
from book.models import Author, Category, Book, Shelf
from django.utils.timezone import now
from book import forms
from book import views


class TestDashboardPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("book:dashboard")

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

        self.assertTemplateUsed(self.response, 'book/dashboard.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.DashboardView)


class TestBookListPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("book:book-list")

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

        self.assertTemplateUsed(self.response, 'book/book_list.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.BooksListView)


class TestCategoryListPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("book:category-list")

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

        self.assertTemplateUsed(self.response, 'book/category_list.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.CategoryListView)


class TestShelfListPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("book:shelf-list")

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

        self.assertTemplateUsed(self.response, 'book/shelf_list.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, views.ShelfListView)


class TestCategoryCreatePage(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Category

        self.creation_form = forms.CategoryCreationForm

        self.url = reverse("book:category-create")

        self.view = views.CategoryCreateView

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

        self.assertTemplateUsed(self.response, 'book/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_crategory_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_create_category_view(self):

        self.login_user()

        data = {
            'name': 'Information and technology'
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

    def test_form_inputs(self):

        self.login_user()

        self.assertContains(self.response, '<input', 2)

        self.assertContains(self.response, 'type="text"', 1)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="submit"', 1)


class TestBookCreatePage(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Book

        self.creation_form = forms.BookCreationAddForm

        self.url = reverse("book:book-create")

        self.view = views.BookCreateView

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

        self.assertTemplateUsed(self.response, 'book/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_book_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_create_book_view(self):

        self.login_user()

        author = mommy.make("Author")

        category = mommy.make("Category")

        shelf = mommy.make("Shelf")

        data = {
            'name': 'War and Peace',
            'author': [author.pk, ],
            'category': category.pk,
            'amount': 12,
            'price': 22.22,
            'available': True,
            'description': "This is a great book",
            'shelf': shelf.pk,
        }

        self.response = self.client.post(self.url, data)

        self.assertEqual(self.response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

    def test_form_inputs(self):

        self.login_user()

        self.assertContains(self.response, '<input', 5)

        self.assertContains(self.response, '<select', 3)

        self.assertContains(self.response, 'type="text"', 1)

        self.assertContains(self.response, 'type="file"', 1)

        self.assertContains(self.response, 'type="number"', 2)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="submit"', 1)

        self.assertContains(self.response, 'type="reset"', 1)


class TestAuthorCreatePage(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Author

        self.creation_form = forms.AuthorCreationForm

        self.url = reverse("book:author-create")

        self.view = views.AuthorCreateView

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

        self.assertTemplateUsed(self.response, 'book/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_author_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_create_author_view(self):

        self.login_user()

        data = {
            'first_name': 'john',
            'last_name': 'doe',
            'born': '03/08/2019 14:00'
        }

        self.response = self.client.post(self.url, data)

        self.assertEqual(self.response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

    def test_form_inputs(self):

        self.login_user()

        self.assertContains(self.response, '<input', 6)

        self.assertContains(self.response, 'type="text"', 4)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="file"', 1)

        self.assertContains(self.response, 'type="submit"', 1)

        self.assertContains(self.response, 'type="reset"', 1)


class TestShelfCreatePage(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Shelf

        self.creation_form = forms.ShelfCreationForm

        self.url = reverse("book:shelf-create")

        self.view = views.ShelfCreateView

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

        self.assertTemplateUsed(self.response, 'book/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_shelf_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_create_shelf_view(self):

        self.login_user()

        data = {
            'name': 'Shelf-2',
            'active': True,

        }

        self.response = self.client.post(self.url, data)

        self.assertEqual(self.response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

    def test_form_inputs(self):

        self.login_user()

        self.assertContains(self.response, '<input', 2)

        self.assertContains(self.response, 'type="text"', 1)

        self.assertContains(self.response, 'type="hidden"', 1)

        self.assertContains(self.response, 'type="submit"', 1)

        self.assertContains(self.response, 'type="reset"', 1)


class TestBookUpdateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Book

        self.instance = mommy.make(self.model)

        self.creation_form = forms.BookCreationAddForm

        self.url = reverse("book:book-update",
                           kwargs={"slug": self.instance.slug})

        self.view = views.BookUpdateView

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

        self.assertTemplateUsed(self.response, 'book/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_book_update_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_update_book_view(self):

        self.login_user()

        author = mommy.make("Author")

        category = mommy.make("Category")

        shelf = mommy.make("Shelf")

        data = {
            'name': 'War and Peace',
            'author': [author.pk, ],
            'category': category.pk,
            'amount': 12,
            'price': 22.22,
            'available': True,
            'description': "This is a great book",
            'shelf': shelf.pk,
        }

        self.client.post(reverse('book:book-create'), data)

        data['name'] = 'updated book name'

        self.response = self.client.post(self.url, data)

        self.assertEqual(self.response.status_code, 302)

        expected = "updated book name"

        actual = str(Book.objects.get(slug=self.instance.slug))

        self.assertEqual(actual, expected)


class TestAuthorUpdateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Author

        self.instance = mommy.make(self.model)

        self.creation_form = forms.AuthorCreationForm

        self.url = reverse("book:author-update",
                           kwargs={"pk": self.instance.pk})

        self.view = views.AuthorUpdateView

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

        self.assertTemplateUsed(self.response, 'book/form.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func.view_class, self.view)

    def test_author_update_form(self):

        self.login_user()

        form = self.response.context.get("form")

        self.assertIsInstance(form, self.creation_form)

    def test_csrf(self):

        self.login_user()

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_update_book_view(self):

        self.login_user()

        data = {
            'first_name': 'john',
            'last_name': 'doe',
            'born': '03/08/2019 14:00'
        }

        self.client.post(reverse('book:author-create'), data)

        data['first_name'] = 'updated author name'

        self.response = self.client.post(self.url, data)

        self.assertEqual(self.response.status_code, 302)

        expected = "updated author name"

        actual = Author.objects.last().first_name

        self.assertEqual(actual, expected)


class TestCategoryUpdateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Category

        self.instance = mommy.make(self.model)

        self.url = reverse('book:category-update',
                           kwargs={'pk': self.instance.pk})

        self.view = views.category_update_view

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

    def test_category_book_view(self):

        self.login_user()

        data = {
            'name': 'Information and technology'
        }

        response = self.client.post(reverse("book:category-create"), data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

        obj = self.model.objects.last()

        data['name'] = 'updated category name'

        response = self.client.post(
            reverse('book:category-update', kwargs={'pk': obj.pk}), data)

        expected = "updated category name"

        actual = self.model.objects.last().name

        self.assertEqual(actual, expected)


class TestShelfUpdateView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Shelf

        self.instance = mommy.make(self.model)

        self.url = reverse('book:shelf-update',
                           kwargs={'pk': self.instance.pk})

        self.view = views.shelf_update_view

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

        data = {
            'name': 'Information and technology'
        }

        response = self.client.post(reverse("book:shelf-create"), data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(self.model.objects.exists())

        obj = self.model.objects.last()

        data['name'] = 'updated shelf name'

        response = self.client.post(
            reverse('book:shelf-update', kwargs={'pk': obj.pk}), data)

        expected = "updated shelf name"

        actual = self.model.objects.last().name

        self.assertEqual(actual, expected)


class TestBookDeleteView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Book

        self.instance = mommy.make(self.model)

        self.url = reverse('book:book-delete',
                           kwargs={'pk': self.instance.pk})

        self.view = views.book_delete_view

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


class TestCategoryDeleteView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Category

        self.instance = mommy.make(self.model)

        self.url = reverse('book:category-delete',
                           kwargs={'pk': self.instance.pk})

        self.view = views.category_delete_view

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


class TestShelfDeleteView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Shelf

        self.instance = mommy.make(self.model)

        self.url = reverse('book:shelf-delete',
                           kwargs={'pk': self.instance.pk})

        self.view = views.shelf_delete_view

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


class TestAuthorDeleteView(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = Author

        self.instance = mommy.make(self.model)

        self.url = reverse('book:author-delete',
                           kwargs={'pk': self.instance.pk})

        self.view = views.author_delete_view

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

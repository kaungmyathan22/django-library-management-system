from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.db.models.signals import post_save
from model_mommy import mommy
from book.models import Book, Category, Author, Shelf, image_upload_path
import mock

class TestBookModel(TestCase):

    def setUp(self):

        self.model_type = Book

        self.model = mommy.make(self.model_type)

    def test_instance(self):

        self.assertTrue(isinstance(self.model, self.model_type))

    def test_str(self):

        self.assertEqual(str(self.model), self.model.name)

    def test_slug(self):

        self.assertTrue(len(self.model.slug) > 1)

    def test_count(self):

        for _ in range(4):

            mommy.make(self.model_type)

        actual_result = self.model_type.objects.count()

        expected_result = 5

        self.assertEqual(actual_result, expected_result)

    def test_post_save_signal(self):

        with mock.patch('book.signals.object_post_save_reciever', autospec=True) as mocked_handler:
            
            post_save.connect(mocked_handler, sender=Book, dispatch_uid='test_cache_mocked_handler')
            
            model = mommy.make(self.model_type)

            self.assertEquals(mocked_handler.call_count, 2)  # post save fire when creating and saving
            

class TestAuthorModel(TestCase):

    def setUp(self):

        self.model_type = Author

        self.model = mommy.make(self.model_type)

    def test_instance(self):

        self.assertTrue(isinstance(self.model, self.model_type))

    def test_str(self):

        actual = str(self.model)

        expeced = f'{self.model.first_name} {self.model.last_name}'

        self.assertEqual(actual, expeced)

    def test_count(self):

        for _ in range(4):

            mommy.make(self.model_type)

        actual_result = self.model_type.objects.count()

        expected_result = 5

        self.assertEqual(actual_result, expected_result)

    def test_author_books_count(self):

        author = mommy.make(self.model_type)

        for _ in range(4):

            model = mommy.make(Book)

            model.author.add(author)

            model.save()

        actual = author.books.count()

        expected = 4

        self.assertEqual(actual, expected)

    def test_image_upload_path(self):

        filename = image_upload_path(self.model, 'hello.png')

        self.assertNotEqual(filename, 'hello.png')


class TestCategoryModel(TestCase):

    def setUp(self):

        self.model_type = Category

        self.model = mommy.make(self.model_type)

    def test_instance(self):

        self.assertTrue(isinstance(self.model, self.model_type))

    def test_str(self):

        self.assertEqual(str(self.model), self.model.name)

    def test_slug(self):

        self.assertTrue(len(self.model.slug) > 1)

    def test_count(self):

        for _ in range(4):

            mommy.make(self.model_type)

        actual_result = self.model_type.objects.count()

        expected_result = 5

        self.assertEqual(actual_result, expected_result)


class TestShelfModel(TestCase):

    def setUp(self):

        self.model_type = Shelf

        self.model = mommy.make(self.model_type)

    def test_instance(self):

        self.assertTrue(isinstance(self.model, self.model_type))

    def test_str(self):

        self.assertEqual(str(self.model), self.model.name)

    def test_count(self):

        for _ in range(4):

            mommy.make(self.model_type)

        actual_result = self.model_type.objects.count()

        expected_result = 5

        self.assertEqual(actual_result, expected_result)

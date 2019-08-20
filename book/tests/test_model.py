from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from book.models import Book, Category, Author


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

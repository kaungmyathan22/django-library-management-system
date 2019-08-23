import unittest
from django.test import TestCase
from book.models import Book
from model_mommy import mommy
from .random_string_generator import random_string_generator
from .unique_slug_field_generator import unique_slug_generator

class TestStringMethods(TestCase):

    def test_random_string_generator_with_default_length(self):

        default_str_length =random_string_generator()

        actual = len(default_str_length)

        expected = 10

        self.assertEquals(actual, expected)
    
    def test_random_string_generator_with_custom_length(self):
    
        default_str_length =random_string_generator(size=20)

        actual = len(default_str_length)

        expected = 20

        self.assertEquals(actual, expected)

    def test_unique_slug_generator(self):
    
        model = mommy.make(Book)

        old_slug = model.slug

        new_slug = unique_slug_generator(model)


        self.assertNotEqual(old_slug, new_slug)

    

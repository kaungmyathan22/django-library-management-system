from django.test import TestCase
from model_mommy import mommy
from issue.models import Issue


class TestIssueModel(TestCase):
    def setUp(self):
    
        self.model_type = Issue

        self.model = mommy.make(self.model_type)

    def test_instance(self):

        self.assertTrue(isinstance(self.model, self.model_type))

    def test_str(self):

        expected = str(self.model)

        actual = f'{self.model.member} borrow {self.model.book}'

        self.assertEqual(actual, expected)

    def test_count(self):

        for _ in range(4):

            mommy.make(self.model_type)

        actual_result = self.model_type.objects.count()

        expected_result = 5

        self.assertEqual(actual_result, expected_result)



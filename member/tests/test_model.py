from django.test import TestCase
from model_mommy import mommy
from member.models import Member, image_upload_path
from django.db.models.signals import post_save
import mock

class TestMemberModel(TestCase):

    def setUp(self):

        self.model_type = Member

        self.model = mommy.make(self.model_type)

    def test_instance(self):

        self.assertTrue(isinstance(self.model, self.model_type))

    def test_str(self):

        actual = f'{self.model.first_name} {self.model.last_name} '

        expected = str(self.model)

        self.assertEqual(actual, expected)

    def test_image_upload_path(self):
    
        filename = image_upload_path(self.model, 'hello.png')

        self.assertNotEqual(filename, 'hello.png')

    def test_post_save_signal(self):
    
        with mock.patch('member.signals.object_post_save_reciever', autospec=True) as mocked_handler:
            
            post_save.connect(mocked_handler, sender=self.model_type, dispatch_uid='test_cache_mocked_handler')
            
            model = mommy.make(self.model_type)

            self.assertEquals(mocked_handler.call_count, 2)  # post save fire when creating and saving

    def test_slug(self):

        self.assertTrue(len(self.model.slug) > 1)

    def test_count(self):

        for _ in range(4):

            mommy.make(self.model_type)

        actual_result = self.model_type.objects.count()

        expected_result = 5

        self.assertEqual(actual_result, expected_result)

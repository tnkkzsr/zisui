from django.test import TestCase
from .models import ZisuiPost
from django.urls import reverse


# Create your tests here.

class brogTestCase(TestCase):
    def setUp(self):
        obj = ZisuiPost(title="yakiniku")
        obj.save()

    def test_saved_single_object(self):
        qs_counter = ZisuiPost.objects.count()
        self.assertEqual(qs_counter, 1)


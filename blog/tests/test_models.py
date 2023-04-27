from django.test import TestCase
from blog.models import ZisuiPost

class PostModelTests(TestCase):

    def test_is_empty(self):
        saved_posts = ZisuiPost.objects.all()
        self.assertEqual(saved_posts.count(),0)

    def test_is_count_one(self):
        post = ZisuiPost(title="オムライス")
        post.save()
        saved_post=ZisuiPost.objects.all()
        self.assertEqual(saved_post.count(),1)

    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = ZisuiPost()
        title = 'test_title_to_retrieve'
        image = "images/1087_01.jpg"
        post.title = title
        post.image = image
        post.save()
        saved_posts = ZisuiPost.objects.all()
        actual_post = saved_posts[0]
        self.assertEqual(actual_post.title, title)
        self.assertEqual(actual_post.image, image)
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )

    def test_post_list_view(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        url = reverse('blog:post_detail', args=[self.post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

    def test_post_create_view(self):
        url = reverse('blog:post_create')
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_create.html')

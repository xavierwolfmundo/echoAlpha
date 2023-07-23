from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from calendar.models import Event
from digital_storefront.models import Product

class PostListViewTest(TestCase):
    def test_post_list_view(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class EventListViewTest(TestCase):
    def test_event_list_view(self):
        url = reverse('events:event_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ProductListViewTest(TestCase):
    def test_product_list_view(self):
        url = reverse('digital_storefront:product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

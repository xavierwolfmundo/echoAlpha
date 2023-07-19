from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView
from calendar.views import EventListView
from digital_storefront.views import ProductListView

class TestUrls(SimpleTestCase):
    def test_blog_url(self):
        url = reverse('blog:post_list')
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_events_url(self):
        url = reverse('events:event_list')
        self.assertEqual(resolve(url).func.view_class, EventListView)

    def test_digital_storefront_url(self):
        url = reverse('digital_storefront:product_list')
        self.assertEqual(resolve(url).func.view_class, ProductListView)

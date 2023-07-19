from django.test import TestCase
from django.urls import reverse

class IntegrationTest(TestCase):
    def test_blog_post_list_integration(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to My Blog")

    def test_events_event_list_integration(self):
        url = reverse('events:event_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Upcoming Events")

    def test_digital_storefront_product_list_integration(self):
        url = reverse('digital_storefront:product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Available Products")

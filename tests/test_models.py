from django.test import TestCase
from blog.models import Post
from events.models import Event
from digital_storefront.models import Product

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')

class EventModelTest(TestCase):
    def test_event_creation(self):
        event = Event.objects.create(title='Test Event', description='This is a test event.')
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.description, 'This is a test event.')

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name='Test Product', price=9.99)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 9.99)

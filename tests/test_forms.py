from django.test import TestCase
from blog.forms import PostForm
from calendar.forms import EventForm
from digital_storefront.forms import ProductForm

class PostFormTest(TestCase):
    def test_valid_post_form(self):
        data = {'title': 'Test Post', 'content': 'This is a test post.'}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_post_form(self):
        data = {'title': '', 'content': ''}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())

class EventFormTest(TestCase):
    def test_valid_event_form(self):
        data = {'title': 'Test Event', 'description': 'This is a test event.'}
        form = EventForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_event_form(self):
        data = {'title': '', 'description': ''}
        form = EventForm(data=data)
        self.assertFalse(form.is_valid())

class ProductFormTest(TestCase):
    def test_valid_product_form(self):
        data = {'name': 'Test Product', 'price': 9.99}
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_product_form(self):
        data = {'name': '', 'price': -1}
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())

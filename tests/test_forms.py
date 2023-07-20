# project/tests/test_forms.py

import pytest
from django.test import TestCase
from project.blog.forms import PostForm
from project.calendar.forms import EventForm
from project.digital_storefront.forms import ProductForm

@pytest.mark.django_db
class TestForms(TestCase):
    def test_post_form_valid_data(self):
        form_data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_invalid_data(self):
        form_data = {
            'title': '',  # Title is required
            'content': 'This is a test post content.',
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_event_form_valid_data(self):
        form_data = {
            'title': 'Test Event',
            'description': 'This is a test event description.',
            'start_date': '2023-07-30',
            'end_date': '2023-08-01',
            'location': 'Test Location',
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_event_form_invalid_data(self):
        form_data = {
            'title': 'Test Event',
            'description': 'This is a test event description.',
            'start_date': '',  # Start date is required
            'end_date': '2023-08-01',
            'location': 'Test Location',
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_product_form_valid_data(self):
        form_data = {
            'name': 'Test Product',
            'price': 99.99,
            'description': 'This is a test product description.',
            'category': 'Test Category',
            'tags': 'test, product',
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_data(self):
        form_data = {
            'name': '',  # Name is required
            'price': 99.99,
            'description': 'This is a test product description.',
            'category': 'Test Category',
            'tags': 'test, product',
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())

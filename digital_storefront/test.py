# project/digital_storefront/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Product
from .forms import ProductForm


class ProductTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=10.99,
            description='This is a test product.',
            category='Test Category',
        )

    def test_product_creation(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.description, 'This is a test product.')
        self.assertEqual(product.category, 'Test Category')


class ProductFormTests(TestCase):
    def test_product_form_valid(self):
        form_data = {
            'name': 'Test Product',
            'price': 10.99,
            'description': 'This is a test product.',
            'category': 'Test Category',
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid(self):
        form_data = {
            'name': '',
            'price': 10.99,
            'description': 'This is a test product.',
            'category': 'Test Category',
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())


class DigitalStorefrontViewsTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=10.99,
            description='This is a test product.',
            category='Test Category',
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_product_detail_view(self):
        response = self.client.get(
            reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    # Add more view tests as needed


class DigitalStorefrontURLTests(TestCase):
    def test_product_list_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        product = Product.objects.create(
            name='Test Product',
            price=10.99,
            description='This is a test product.',
            category='Test Category',
        )
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    # Add more URL tests as needed

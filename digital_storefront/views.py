from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductListView(ListView):
    model = Product
    template_name = 'digital_storefront/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'digital_storefront/product_detail.html'
    context_object_name = 'product'

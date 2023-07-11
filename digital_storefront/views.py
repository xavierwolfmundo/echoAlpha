from django.views.generic import ListView, DetailView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductListView(ListView):
    model = Product
    template_name = 'digital_storefront/product_list.html'
    context_object_name = 'products'
    paginate_by = 10  # Set the number of products per page

class ProductDetailView(DetailView):
    model = Product
    template_name = 'digital_storefront/product_detail.html'
    context_object_name = 'product'

    # Require login for accessing product details
    # Remove this if you want to allow public access
    # or customize as per your authentication requirements
    # (e.g., only allow authenticated users who have purchased the product)
    mixins = [LoginRequiredMixin]

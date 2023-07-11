from django.urls import path
from .views import PostListView, PostDetailView
from digital_storefront.views import ProductDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

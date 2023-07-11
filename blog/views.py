from django.views.generic import ListView, DetailView
from .models import Post
from digital_storefront.models import Product
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Set the number of posts per page

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get related digital products based on post categories and tags
        related_products = Product.objects.filter(
            Q(categories__in=self.object.categories.all()) | Q(tags__in=self.object.tags.all())
        ).exclude(pk=self.object.product.pk)[:5]  # Exclude current post's associated product
        context['related_products'] = related_products

        return context

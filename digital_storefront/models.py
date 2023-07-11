from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    # Additional fields
    image = models.ImageField(upload_to='product_images/')
    metadata = models.JSONField(blank=True, null=True)
    # Add any other fields relevant to your digital products

    def __str__(self):
        return self.title

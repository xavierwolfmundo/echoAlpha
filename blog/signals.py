from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        # Perform any necessary actions when a new post is created
        pass
    else:
        # Perform any necessary actions when an existing post is saved
        pass

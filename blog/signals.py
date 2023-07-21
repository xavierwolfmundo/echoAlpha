from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        # Perform any necessary actions when a new post is created
        # For example, you can send an email notification to the author
        # or perform any other actions needed for new posts.
        pass
    else:
        # Perform any necessary actions when an existing post is saved
        # For example, you can update some other related models
        # or trigger other tasks based on changes to the post.
        pass

# Import other models if needed for further signal handling
# from .models import Comment, Category, Tag

# Add additional signal handlers here for other models if required
# For example, to handle comments:
# @receiver(post_save, sender=Comment)
# def comment_saved(sender, instance, created, **kwargs):
#     if created:
#         # Perform any necessary actions when a new comment is created
#         pass
#     else:
#         # Perform any necessary actions when an existing comment is saved
#         pass

# Similar signal handlers can be added for other models like Category and Tag
# Remember to connect these signal handlers to their respective models using the @receiver decorator.


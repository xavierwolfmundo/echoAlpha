from django.apps import AppConfig


class BlogConfig(AppConfig):
    # Define the default primary key type for models.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the app. This should match the name of the app directory.
    name = 'blog'

    # The ready() method is called as soon as the app registry is fully populated.
    def ready(self):
        # Import the signals module to ensure the signals are connected.
        import blog.signals

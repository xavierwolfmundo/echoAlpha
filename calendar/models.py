from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    driving_directions = models.TextField()
    # Add other fields specific to an event

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

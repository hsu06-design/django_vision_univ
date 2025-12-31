from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # This will store your photos
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    # This adds the date automatically
    date_added = models.DateTimeField(default=timezone.now)
    tech = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
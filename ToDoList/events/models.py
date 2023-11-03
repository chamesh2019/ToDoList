from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_at = models.DateTimeField(null=True)
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Chirp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

class Reply(Chirp):
    parent = models.ForeignKey(Chirp, on_delete=models.CASCADE, related_name="replies")
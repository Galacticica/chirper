from django.db import models
from chirps.models import Chirp

class Reply(Chirp):
    parent = models.ForeignKey(Chirp, on_delete=models.CASCADE, related_name="replies")
    reply_content = models.CharField(max_length=255)

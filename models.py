from django.db import models
"from ___ import user"

class Chirps(models.Model):
    user = user
    content = models.CharField(max_length=250)
    reply = models.CharField(primary_key=True)
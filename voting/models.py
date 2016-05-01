from django.db import models

class Quote(models.Model):
    drug = models.CharField(max_length=40, unique=True)
    branch = models.CharField(max_length=40, unique=True)
    price = models.IntegerField(default=0)

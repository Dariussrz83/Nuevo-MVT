from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    minor = models.BooleanField()

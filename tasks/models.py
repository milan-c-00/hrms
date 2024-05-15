from django.db import models
from django.db.models import Model

class Task(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='')
    date = models.DateField(auto_now=True)

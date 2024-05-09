from django.db import models

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=255),
    # employee = models.ForeignKey(Employee, null=True, blank=True),
    file = models.FileField(upload_to='documents/'),

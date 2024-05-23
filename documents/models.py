from django.db import models

from employees.models import Employee


# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='documents/')
    is_general = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def doc_name(self):
        return self.file.name[10:]

    def file_size_mb(self):
        size = self.file.size
        data = {}
        if size < 1024:
            data['size'] = size
            data['unit'] = 'B'
            return data
        elif size < (1024 * 1024):
            data['size'] = round(size / 1024, 2)
            data['unit'] = 'KB'
            return data
        elif size < (1024 * 1024 * 1024):
            data['size'] = round(size / (1024*1024), 2)
            data['unit'] = 'MB'
            return data
        else:
            data['size'] = round(size / (1024*1024*1024), 2)
            data['unit'] = 'GB'

    def doc_type(self):
        parts = self.file.name.rsplit('.', 1)
        if len(parts) == 1:
            return ""
        else:
            return parts[1].lower()

    class Meta:
        ordering = ['-created_at']

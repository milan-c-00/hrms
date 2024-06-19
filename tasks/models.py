from django.db import models
from employees.models import Employee

class Task(models.Model):
    title = models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    start=models.DateField()
    end=models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    importance=models.CharField(max_length=30)

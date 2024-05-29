from django.db import models
from employees.models import Employee

class Task(models.Model):
    title = models.CharField(max_length=30, verbose_name='Task Name')
    status=models.CharField(max_length=30)
    start=models.DateTimeField()
    end=models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    #employee=models.CharField(max_length=30)
    importance=models.CharField(max_length=30)

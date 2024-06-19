from django.db import models
from employees.models import Employee

class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    professional_email=models.CharField(max_length=50)
    notes=models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True,blank=True)


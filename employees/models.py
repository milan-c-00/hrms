from django.db import models

class Employee(models.Model):
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    date_of_birth=models.DateField()

    personal_email=models.CharField(max_length=50)
    professional_email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    educational_background=models.CharField(max_length=200)
    
    job_objective=models.CharField(max_length=200)

    file=models.FileField(upload_to='media/')
    file_name = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField()

    status_type=models.CharField(max_length=50)
    internship=models.CharField(max_length=50)
    last_position=models.CharField(max_length=50)
    present_position=models.CharField(max_length=50)

    constract_start_date=models.DateField()
    contract_expiration_date=models.DateField()

    salary=models.CharField(max_length=50)
    changes=models.CharField(max_length=50)
    financial_bonuses=models.CharField(max_length=50)
    date1=models.DateTimeField()
    other_bonuses=models.CharField(max_length=50)
    date2=models.DateTimeField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"    


    

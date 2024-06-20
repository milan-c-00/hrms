from django.db import models
#
# class Employee(models.Model):
#     image=models.ImageField(upload_to='images/',null=True,blank=True)
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     title=models.CharField(max_length=50)
#     date_of_birth=models.DateField()
#
#     personal_email=models.CharField(max_length=50)
#     professional_email=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)
#     phone=models.CharField(max_length=50)
#
#     educational_background=models.CharField(max_length=200)
#
#     job_objective=models.CharField(max_length=200)
#
#     file=models.FileField(upload_to='media/')
#     file_name = models.CharField(max_length=50)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     file_size = models.IntegerField()
#
#     status_type=models.CharField(max_length=50)
#     internship=models.CharField(max_length=50)
#     last_position=models.CharField(max_length=50)
#     present_position=models.CharField(max_length=50)
#
#     constract_start_date=models.DateField()
#     contract_expiration_date=models.DateField()
#
#     salary=models.CharField(max_length=50)
#     changes=models.CharField(max_length=50)
#     financial_bonuses=models.CharField(max_length=50)
#     date1=models.DateTimeField()
#     other_bonuses=models.CharField(max_length=50)
#     date2=models.DateTimeField()


class Employee(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    position = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    personal_email = models.CharField(max_length=255, null=True, blank=True)
    professional_email = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)


class Education(models.Model):
    school = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    employee = models.ForeignKey(Employee, name='education', on_delete=models.CASCADE)


class WorkExperience(models.Model):
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, name='work_experience', on_delete=models.CASCADE)


class Contract(models.Model):
    status = models.CharField(max_length=255)
    internship = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.FloatField()
    employee = models.ForeignKey(Employee, name='contract', on_delete=models.CASCADE)

    

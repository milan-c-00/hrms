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
    phone = models.CharField(max_length=255)
    personal_email = models.EmailField(max_length=255, null=True, blank=True)
    professional_email = models.EmailField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def employee_contract(self):
        return self.contract_set.first()

    def employee_education(self):
        return self.education_set.first()

    def employee_work_experience(self):
        return self.workexperience_set.first()

    def soft_skills(self):
        return self.skill_set.filter(skill_type='soft')

    def software_skills(self):
        return self.skill_set.filter(skill_type='software')

    def notes(self):
        return self.note_set


class Education(models.Model):
    school = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class WorkExperience(models.Model):
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Contract(models.Model):
    status = models.CharField(max_length=255)
    internship = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Note(models.Model):
    note = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

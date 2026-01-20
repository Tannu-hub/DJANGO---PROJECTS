from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name= models.CharField(max_length=30)
    rollno=models.IntegerField()
    subject = models.CharField(max_length=30)
    



class EmpoloyeeModel(models.Model):
    Emp_name = models.CharField(max_length=50)
    Emp_id = models.IntegerField()
    Dpt_no = models.IntegerField()
    is_active = models.BooleanField(default=False)


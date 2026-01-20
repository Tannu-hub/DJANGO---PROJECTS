from django.db import models

# Create your models here.


class EmpolyeeModel(models.Model):
    E_name = models.CharField(max_length=50)
    E_Email = models.EmailField()
    city = models.CharField(max_length=100)
    E_Address = models.TextField()
    Company = models.CharField(max_length=100)
    Sallary = models.IntegerField()
    Jobrole = models.CharField(default='NA', max_length=100,)

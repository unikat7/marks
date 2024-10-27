from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255,blank=False,null=True)
    address=models.CharField(max_length=255,blank=False,null=True)
    semester=models.CharField(max_length=255,blank=False,null=True)

class Teacher(models.Model):
    name=models.CharField(max_length=255,blank=False,null=True)
    email=models.CharField(max_length=255,blank=False,null=True)
    password=models.CharField(max_length=255,blank=False,null=True)
    def set_password(self,password):
        self.password=make_password(password)








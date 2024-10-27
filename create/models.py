from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255,blank=False,null=True)
    address=models.CharField(max_length=255,blank=False,null=True)
<<<<<<< HEAD
    semester=models.IntegerField(blank=False,null=False)
=======
    semester = models.IntegerField(blank=False, null=True)
>>>>>>> 306fdfbc81093ff89e5da835419c1f129f2e36f0

class Teacher(models.Model):
    name=models.CharField(max_length=255,blank=False,null=True)
    email=models.CharField(max_length=255,blank=False,null=True)
    password=models.CharField(max_length=255,blank=False,null=True)
    def set_password(self,password):
        self.password=make_password(password)


class Semester1(models.Model):
    digital=models.IntegerField(null=False,blank=False)
    cprogramming=models.IntegerField(null=False,blank=False)
    cfa=models.IntegerField(null=False,blank=False)
    english=models.IntegerField(null=False,blank=False)








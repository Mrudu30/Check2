from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .manager import *
# Create your models here.
class Subjects(models.Model):
    name  = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.name
    
class course(models.Model):
    name = models.CharField(max_length=15)
    subject = models.ManyToManyField(Subjects)
    
    def __str__(self):
        return self.name 
    
class Textbooks(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name    
    
class Parents(models.Model):
    father_name = models.CharField(max_length=20,null=True,default='name not given')
    mother_name = models.CharField(max_length=20,null=True,default='name not given')
    guardian_name = models.CharField(max_length=20,null=True,default='name not given')
    ph1 = models.CharField(max_length=10,null=False)
    ph2 = models.CharField(max_length=10,null=True,default='not given')
    mail1 = models.EmailField(null=False)
    mail2 = models.EmailField(null=True,default='xyz@ght.com')     

class Exam(models.Model):
    date_test_given = models.DateField(null=False,default=timezone.now)
    textbook = models.ManyToManyField(Textbooks)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
       
class Student(AbstractUser):
    ph_no = models.CharField(max_length=10,unique=True)
    leaving_date= models.DateField(null=True)
    course = models.ForeignKey(course,null=False,on_delete=models.CASCADE,default=1)
    parent = models.ForeignKey(Parents,null=True,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,null=True,on_delete=models.CASCADE)
    
    objects = studentmanager()
    
    REQUIRED_FIELDS = ['password','first_name','last_name','ph_no','date_joined']
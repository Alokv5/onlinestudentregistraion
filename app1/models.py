from django.db import models
import datetime

class adminModel(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)



class New_shedule(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    fee=models.FloatField()
    duration=models.CharField(max_length=50)

class Student(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=15,default=not None)

class CourseModel(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    facutly=models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    fee = models.FloatField()
    duration = models.CharField(max_length=50)
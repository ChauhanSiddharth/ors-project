from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')))
    usertype = models.CharField(max_length=15, choices=(('member', 'member'), ('instructor', 'instructor'), ('administrator', 'administrator')))
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    contact = models.IntegerField()
    qualification = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='media/image')
    resume = models.FileField(upload_to='media/resume')
    joiningdate = models.DateField()

    def __str__(self):
        return self.firstname

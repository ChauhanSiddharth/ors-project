from __future__ import unicode_literals

from django.db import models
from login.models import UserProfile
from django.contrib.auth.models import User
import datetime
# Create your models here.

class course_details(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/image')
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=10,choices=(('active','active'),('deactive','deactive')))
    duration = models.CharField(max_length=10)
    fees = models.IntegerField()

    def __str__(self):
        return self.title # or convert kari ne print karava pade

class instructor_course(models.Model):
    course_id = models.ForeignKey(course_details)
    instructor_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.course_id) + str(self.instructor_id)

class member_course(models.Model):
    course_id = models.ForeignKey(course_details)
    member_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.course_id) + str(self.member_id)

class material(models.Model):
    course_id = models.ForeignKey(instructor_course)
    mname = models.CharField(max_length=20,null=False)
    date = models.DateField(default=datetime.date.today(), null=True)
    files = models.FileField(upload_to='media/material')

    def __unicode__(self):
        return str(self.mname)

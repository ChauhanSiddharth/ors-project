from __future__ import unicode_literals

from django.db import models

# Create your models here.

from login.models import User
from course.models import course_details,instructor_course

class Class_Master(models.Model):
	class_id = models.IntegerField(primary_key=True,null=False)
	class_name = models.CharField(max_length=20,null=False)
	course_id = models.ForeignKey(course_details)
	Instructor_id = models.ForeignKey(instructor_course)
	schedule_startdate = models.DateField()
	status = models.CharField(max_length=10,null=False,choices=(('Active','Active'),('Deactive','Deactive')))
	Class_completion_status = models.CharField(max_length=10,null=False,choices=(('Started','Started'),('Panding','Panding'),('Cancelled','Cancelled'),('Completed','Completed')))
	Extra_notes = models.CharField(max_length=255,null=False)
	Dcreated = models.DateTimeField()

	def __unicode__(self):
		return str(self.class_name)

class Class_Member(models.Model):
	class_member_id = models.IntegerField(primary_key=True,null=False)
	class_id = models.ForeignKey(Class_Master)
	member_id = models.ForeignKey(User)

	def __unicode__(self):
		return str(self.class_member_id)
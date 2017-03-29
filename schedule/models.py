from __future__ import unicode_literals

from django.db import models

from class_details.models import Class_Master

# Create your models here.
class Schedule_Master(models.Model):
	Schedule_master_id = models.IntegerField(primary_key=True,null=False)
	Class_id = models.ForeignKey(Class_Master)
	Schedule_datetime = models.DateTimeField()
	Schedule_description = models.CharField(max_length=255,null=False)
	Schedule_title = models.CharField(max_length=20,null=False)
	Class_held_status = models.CharField(max_length=20,null=False,choices=(('Pending','Pending'),('Complete','Complete'),('Cancelled','Cancelled')))
	Extra_notes = models.CharField(max_length=255,null=False)
	Status = models.CharField(max_length=20,null=False,choices=(('Active','Active'),('Deactive','Deactive')))

	def __unicode__(self):
		return str(self.Schedule_title)

class Schedule_Syllabus(models.Model):
	Schedule_syllabus_id = models.IntegerField(primary_key=True,null=False)
	Schedule_master_id = models.ForeignKey(Schedule_Master)
	Session_type = models.CharField(max_length=20,null=False,choices=(('Regular','Regular'),('Extra','Extra')))
	Extra_notes = models.CharField(max_length=255,null=False)

	def __unicode__(self):
		return str(self.Session_type)
from __future__ import unicode_literals
from course.models import course_details

from django.db import models
from login.models import User, UserProfile
# Create your models here.

class Orders_Item(models.Model):
	order_item_id = models.IntegerField(null=False,primary_key=True)
	course_Id = models.ForeignKey(course_details)
	member_id = models.ForeignKey(User)
	Total_Amount = models.IntegerField(null=False)

	def __unicode__(self):
		return str(self.order_item_id)

class Orders(models.Model):
	order_id = models.IntegerField(null=False,primary_key=True)
	transaction_id = models.IntegerField(null=False)
	order_item_id = models.ForeignKey(Orders_Item)
	t_date = models.DateField()

	def __unicode__(self):
		return str(self.order_id)
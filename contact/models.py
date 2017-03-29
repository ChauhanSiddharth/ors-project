from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact_Us(models.Model):
    c_id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=20,null=False)
    subject = models.CharField(max_length=20,null=False)
    follow_up = models.CharField(max_length=20,null=False)
    extra_note = models.TextField(max_length=255,null=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
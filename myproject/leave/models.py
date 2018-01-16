# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#class LeaveTypeForm()
REPORTING_SENIOR_CHOICES = [
('Badri','Badri'),
('Jai Srinivasan','Jai Srinivasan')
]

class LeaveForm(models.Model):
	name = models.CharField(max_length=30)
	reporing_senior = models.CharField(max_length=30, choices=REPORTING_SENIOR_CHOICES)
	#leave_type = models.


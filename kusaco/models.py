from django.db import models

from django.utils import timezone

class Article(models.Model):
	written_by = models.CharField(max_length=100)
	genre = models.CharField(max_length  = 50)
	title = models.CharField(max_length = 100)
	date_added = models.DateTimeField(default = timezone.now)
	article = models.TextField()

class Event(models.Model):
	title = models.CharField(max_length=100)
	venue = models.CharField(max_length=200)
	date = models.DateField(blank = True, null = True)
	day = models.CharField(max_length=50)
	time_start = models.TimeField(default=timezone.now)
	time_end = models.TimeField(default=timezone.now)
	description = models.TextField()




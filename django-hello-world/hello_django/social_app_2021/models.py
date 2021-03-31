from django.db import models

# Create your models here.
class UserProfile(models.Model):
	about_me = models.TextField()
	birth_date = models.DateTimeField('birthday')
	fav_movies = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	photo_url = models.CharField(max_length=100)

class Group(models.Model):
	name = models.CharField(max_length=100)
	members = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	website_url = models.CharField(max_length=100)

class Event(models.Model):
	creator_name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	start_time = models.DateTimeField('start time')
	end_time = models.DateTimeField('end time')
	location = models.CharField(max_length=100)
	event_title = models.CharField(max_length=100)

class Feed(models.Model):
	feed_type = models.CharField(max_length=100)
	total_likes = models.IntegerField()
	comments = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
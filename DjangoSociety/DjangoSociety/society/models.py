from django.db import models

# Create your models here.

class People(models.Model):
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
	author = models.ForeignKey(People, on_delete=models.CASCADE)

class Event(models.Model):
	description = models.CharField(max_length=100)
	creator_name = models.CharField(max_length=100)
	start_time = models.DateTimeField('start time')
	end_time = models.DateTimeField('end time')
	location = models.CharField(max_length=100)
	event_title = models.CharField(max_length=100)
	author = models.ForeignKey(People, on_delete=models.CASCADE)


class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.title

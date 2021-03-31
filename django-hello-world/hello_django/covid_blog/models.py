from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	details = models.TextField()
	pub_date= models.DateTimeField('date published')

class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.title

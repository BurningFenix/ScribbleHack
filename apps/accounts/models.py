from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils.translation import ugettext_lazy as _

# using AbstractUser as the super class
class SHUser(AbstractUser):
	age = models.IntegerField(null=True)
	about = models.TextField()

class Favorites(models.Model):
	user = models.ManyToManyField(SHUser)
	# for now these are just text fields.
	# if we want, can change them to create links and
	# a seperate table for each interest/favorite item
	books = models.TextField()
	authors = models.TextField()
	artwork = models.TextField()
	artists = models.TextField()
	tv_movies = models.TextField()
	music = models.TextField()
	video_games = models.TextField()
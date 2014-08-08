from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils.translation import ugettext_lazy as _

# using AbstractUser as the super class
class SHUser(AbstractUser):
	age = models.IntegerField(null=True)
	about = models.TextField()
	
	# for now these are just text fields.
	# if we want, can change them to create links and
	# a seperate table for each interest/favorite item
	books = models.TextField(null=True, blank=True)
	authors = models.TextField(null=True, blank=True)
	artwork = models.TextField(null=True, blank=True)
	artists = models.TextField(null=True, blank=True)
	tv_movies = models.TextField(null=True, blank=True)
	music = models.TextField(null=True, blank=True)
	video_games = models.TextField(null=True, blank=True)
from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils.translation import ugettext_lazy as _

# using AbstractUser as the super class
class SHUser(AbstractUser):
	age = models.IntegerField(null=True, blank=True)
	# char and text fields will be stored as '' if blank
	# django will never store them as Null or None
	about = models.TextField(blank=True)
	
	# for now these are just text fields.
	# if we want, can change them to create links and
	# a seperate table for each interest/favorite item
	books = models.TextField(blank=True)
	authors = models.TextField(blank=True)
	artworks = models.TextField(blank=True)
	artists = models.TextField(blank=True)
	tv_movies = models.TextField(blank=True)
	music = models.TextField(blank=True)
	video_games = models.TextField(blank=True)
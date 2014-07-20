from django.db import models
from django.contrib.auth.models import User

class SHUser(models.Model):
	user = models.OneToOneField(User)
	age = models.IntegerField()
	favorite_book = models.CharField(max_length=20, blank=True)
	favorite_hero = models.CharField(max_length=20, blank=True)

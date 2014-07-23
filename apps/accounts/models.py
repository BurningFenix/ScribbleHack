from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils.translation import ugettext_lazy as _

# using AbstractUser as the super class
class SHUser(AbstractUser):
	#user = models.OneToOneField(settings.AUTH_USER_MODEL)
	age = models.IntegerField(null = True)
	favorite_book = models.CharField(max_length=20, blank=True)
	favorite_hero = models.CharField(max_length=20, blank=True)

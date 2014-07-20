from django.db import models
from django.contrib.auth.models import User

class SHUser(models.Model):
	user = models.OneToOneField(User)
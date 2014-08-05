from django.db import models
from apps.accounts.models import SHUser

# this many or may not work out later on
class World(models.Model):
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField()
	creator = models.ForeignKey(SHUser, related_name='creator')
	members = models.ManyToManyField(SHUser, related_name='members')

	class Meta:
		abstract = True

class Work(models.Model):
	name = models.CharField(max_length=100)
	world = models.ManyToManyField(World)
	owner = models.ForeignKey(SHUser, related_name='owner')
	allowed_contrib = models.BooleanField(blank=False)
	contributors = models.ManyToManyField(SHUser, related_name='contributors')
	creation_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

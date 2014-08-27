from django.db import models
from apps.accounts.models import SHUser

# class Writing(models.Model):
# 	name = models.CharField(max_length=100, blank=False)
# 	description = models.TextField()
# 	creator = models.ForeignKey(SHUser, related_name='creator')
# 	members = models.ManyToManyField(SHUser, related_name='members')

class WritingPiece(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(SHUser)
	allowed_contrib = models.BooleanField(blank=False)
	contributors = models.ManyToManyField(SHUser,
		related_name='contributor_to_set')
	creation_date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

class WritingComment(models.Model):
	writing_piece = models.ForeignKey(WritingPiece)
	owner = models.ForeignKey(SHUser)
	isInline = models.BooleanField(default=False)
	start = models.IntegerField(null=True)
	end = models.IntegerField(null=True)
	comment = models.TextField()

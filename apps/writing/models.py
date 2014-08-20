from django.db import models
from apps.universe.models import World, Work
from apps.accounts.models import SHUser

class Writing(World):
	pass

class WritingPiece(Work):
	content = models.TextField()

class WritingComment(models.Model):
	writing_piece = models.ForeignKey(WritingPiece)
	owner = models.ForeignKey(SHUser)
	isInline = models.BooleanField(default=False)
	start = models.IntegerField(null=True)
	end = models.IntegerField(null=True)
	comment = models.TextField()

from django.db import models
from apps.universe import World, Work

class Writing(World):
	pass

class WritingPiece(Work):
	content = models.TextField()
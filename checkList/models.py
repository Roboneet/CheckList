

from django.db import models
from django.utils import timezone

class Item(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	info = models.TextField()
	tick = models.BooleanField(default=False)

	def __str__(self):
		return self.title


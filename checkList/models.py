from django.db import models
from django.utils import timezone

class Item(models.Model):
	
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	info = models.TextField(default="")
	tick = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

	def put_tick(self):
		self.tick = True
		self.save()

	def get_tick(self):
		return self.tick




from django.db import models

from ..users.models import User

class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	users = models.ManyToManyField(User, related_name="courses")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
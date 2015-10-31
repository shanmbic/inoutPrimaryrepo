from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	first = models.CharField(max_length=30)
	current_location = models.CharField(max_length=50)
	#profile_pic = models.ImageField()

class Messages(models.Model):
	content = models.CharField(max_length=500)
	user = models.OneToOneField(UserProfile)
	timestamp = models.DateField(blank=True)


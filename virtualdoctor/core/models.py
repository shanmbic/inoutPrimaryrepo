from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	type_user = models.CharField(max_length=30)
	first = models.CharField(max_length=30)
	current_location = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	#profile_pic = models.ImageField()

class Messages(models.Model):
	content = models.CharField(max_length=500)
	user = models.OneToOneField(UserProfile)
	timestamp = models.DateField(blank=True)

class Medicines(models.Model):
	name = models.CharField(max_length=30)
	disease_associated = 


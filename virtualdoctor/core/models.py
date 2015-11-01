from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	type_user = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	current_location = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	#profile_pic = models.ImageField()

class Messages(models.Model):
	content = models.CharField(max_length=500)
	user = models.OneToOneField(UserProfile)
	timestamp = models.DateField(blank=True)

class Documents(models.Model):
	name = models.CharField(max_length=3000)
	user_belong = models.OneToOneField(UserProfile, related_name='UserCreatedFrom')
	user_shared = models.OneToOneField(UserProfile, related_name='UserSharedWith')
	url = models.CharField(max_length=100)


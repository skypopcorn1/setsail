from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	mobile = models.CharField(max_length=20, blank=True)
	def __str__(self):
		return self.mobile

		class Meta:
			ordering = ['-user']

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	print (**kwargs)
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class YachtClub(models.Model):
	#actual model items
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		default=1,
		related_name='%(class)s_requests_created',
		on_delete=models.CASCADE
		)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-id']

class Yacht(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    vessel_class = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

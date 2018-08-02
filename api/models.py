from django.conf import settings
from django.db import models

# Create your models here.
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

from django.conf import settings
from django.db import models

#Create your models here.
class RaceCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Race(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    race_course = models.OneToOneField(RaceCourse,on_delete=models.CASCADE)
    race_start = models.DateTimeField()
    race_finish = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.user

    class Meta:
        ordering = ['-id']

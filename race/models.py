from django.conf import settings
from django.db import models

class Division(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class Season(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    season_start = models.DateField()
    season_finish = models.DateField()
    division = models.ManyToManyField(Division)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

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
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    race_course = models.ForeignKey(RaceCourse,on_delete=models.CASCADE)
    race_start = models.DateTimeField()
    race_finish = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.race_course) + str(self.race_start)

    class Meta:
        ordering = ['-id']

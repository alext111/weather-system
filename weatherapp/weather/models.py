from django.db import models

class Info(models.Model):

    id = models.IntegerField(primary_key=True)
    day = models.DateField()
    city = models.TextField()
    description = models.TextField()
    temp_max = models.TextField()
    temp_min = models.TextField()
    humidity = models.TextField()


# Create your models here.

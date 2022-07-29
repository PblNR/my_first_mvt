from django.db import models

class relatives(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()
    birthday = models.DateField(max_length=10)
 
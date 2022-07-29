from django.db import models

class Relatives(models.Model):
    name = models.CharField(max_length = 80)
    age = models.IntegerField()
    #birthday = models.DateField(default = 10/10/1950)
 
 #No conseguí hacer que funcione la edad
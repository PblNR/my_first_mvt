from django.db import models

class Relatives(models.Model):
    name = models.CharField(max_length = 80)
    age = models.IntegerField()
    birth_date = models.DateField(default = '1950-10-10')
 
 #No conseguí hacer que funcione la edad
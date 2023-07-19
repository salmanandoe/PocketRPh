from django.db import models

class Medication(models.Model):
    image = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    frequency = models.TextField(max_length=1000)
    indication = models.TextField(max_length=1000)
    

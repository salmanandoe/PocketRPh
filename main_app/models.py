from django.db import models

class Medication(models.Model):
    img = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    route = models.CharField(max_length=50)
    frequency = models.CharField(max_length=1000)
    indication = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Database(models.Model):
    generic_name = models.TextField(max_length=100)
    brand_name = models.TextField(max_length=100)
    uses = models.TextField(max_length=5000)
    how_it_works = models.TextField(max_length=5000)
    side_effects = models.TextField(max_length=5000)
    counseling_points = models.TextField(max_length=5000)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['generic_name']
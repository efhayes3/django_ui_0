from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    school_quality = models.IntegerField()
    crime_level = models.IntegerField()
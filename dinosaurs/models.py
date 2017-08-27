from django.db import models

class Dinosaur(models.Model):
    species = models.TextField()
    teeth = models.TextField()
    
    id = models.IntegerField( primary_key=True ) 
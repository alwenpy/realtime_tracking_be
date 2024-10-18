from django.db import models

# Create your models here.

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is updated

    def __str__(self):
        return f"Location(lat: {self.latitude}, lng: {self.longitude})"

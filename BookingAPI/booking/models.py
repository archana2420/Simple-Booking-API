from django.db import models

# Create your models here.
class Bookings(models.Model):
    slot=models.IntegerField()
    name=models.CharField(max_length=50,default="NA")


    def __str__(self):
        return self.name

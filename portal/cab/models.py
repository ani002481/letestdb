from django.db import models
from main.models import *

class cab(models.Model):
    Servicetype=models.CharField(max_length=250)
    Source=models.CharField(max_length=250)
    Destnation=models.CharField(max_length=250)
    Bookdate=models.DateTimeField()
    Booktime=models.TimeField()
    Pickuptime=models.DateTimeField()
    Driverid=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    fare=models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    comment = models.TextField(max_length=250)
    canceltime = models.TimeField()
    reasonofcan = models.TextField(max_length=250)
    empid = models.ForeignKey(user, on_delete=models.CASCADE)


    def __str__ (self):
        return self.id
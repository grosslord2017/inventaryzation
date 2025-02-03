from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):

    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50, help_text="office, plazma, rivermall, salon_LH2 ....") #office, plazma, rivermall, salon_LH2 ....
    marker = models.CharField(max_length=10, default=None, null=True, help_text="shop, sklad ...") #shop, sklad ...
    address = models.CharField(max_length=200) #shevchenko 390 ....

    def __str__(self):
        return self.name


class Worker(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    job_position = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    work_phone = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return f"{self.surname} {self.name}"


class Item(models.Model):

    name = models.CharField(max_length=50) #mouse, monitor, ets ...
    model = models.CharField(max_length=50)
    serial = models.CharField(max_length=100, default=None, null=True)
    description = models.TextField(blank=True)
    worker = models.ManyToManyField(Worker, default=None, blank=True)
    date_of_purchase = models.DateField(default=None, null=True, blank=True)
    date_of_decommissioned = models.DateField(default=None, null=True, blank=True)
    price = models.FloatField(default=None, null=True, blank=True)
    is_reserve = models.BooleanField(default=False)
    is_decommissioned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.model}"


class History(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    action = models.CharField(max_length=100)
    obj = models.ForeignKey(Item, on_delete=models.DO_NOTHING, default=None)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)



from django.db import models

# Create your models here.

INVENT_GROUP = (
    ("---", "---"),
    ("Автомобілі", "Автомобілі"),
    ("Меблі", "Меблі"),
    ("Будівлі", "Будівлі"),
    ("Орг.техніка", "Орг.техніка"),
    ("Периферія", "Периферія"),
    ("Ноутбуки та ПК", "Ноутбуки та ПК"),
    ("Смартфони та планшети", "Смартфони та планшети"),
    ("Складське обладнання", "Складське обладнання"),
    ("Предмети інтерєру", "Предмети інтерєру")
)

class Inventaryzation(models.Model):

    group = models.CharField(max_length=100, choices=INVENT_GROUP, default="---")
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    inv_numb = models.CharField(max_length=15)
    location = models.CharField(max_length=500)
    responsible = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    date_of_purchase = models.DateField(default=None, null=True, blank=True)
    market_price = models.PositiveIntegerField(default=0) # if do not have price
    date_of_registration = models.DateField(default=None, null=True, blank=True) # if do not have date_of_purchase
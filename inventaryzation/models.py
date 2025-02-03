import datetime

from django.db import models
from datetime import date, datetime
from iris.settings import BASE_DIR

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
    ("Предмети інтерєру", "Предмети інтерєру"),
    ("Мережеве обладнання", "Мережеве обладнання"),
)

OPERATIONS = (
    ("Додавання об'єкта", "Додавання об'єкта"),
    ("Списання", "Списання"),
    ("Зміна МВО", "Зміна МВО"),
)

LOCATIONS = (
    ("Академія (Київ)", "Академія (Київ)"),
    ("Магазин Рівер Мол", "Магазин Рівер Мол"),
    ("Київський офіс", "Київський офіс"),
    ("Іріс (магазин Іріс, Шевченка 390)", "Іріс (магазин Іріс, Шевченка 390)"),
    ("Магазин Дашкевича 19", "Магазин Дашкевича 19"),
    ("Магазин Сумгаїтська 39", "Магазин Сумгаїтська 39"),
    ("Черкаський офіс (каб. Сиром'ятникової)", "Черкаський офіс (каб. Сиром'ятникової)"),
    ("Черкаський офіс (конференц зала+коридор у підвалі)", "Черкаський офіс (конференц зала+коридор у підвалі)"),
    ("Черкаський офіс (каб. Системного адміністратора)", "Черкаський офіс (каб. Системного адміністратора)"),
    ("Черкаський офіс (каб. СБ)", "Черкаський офіс (каб. СБ)"),
    ("Черкаський офіс (каб. Бухгалтерії)", "Черкаський офіс (каб. Бухгалтерії)"),
    ("Черкаський офіс (кухня+кімната відпочинку)", "Черкаський офіс (кухня+кімната відпочинку)"),
    ("Черкаський офіс (каб. операторів)", "Черкаський офіс (каб. операторів)"),
    ("Черкаський офіс (серверна)", "Черкаський офіс (серверна)"),
    ("Основний склад (Давінес, Олвейз)", "Основний склад (Давінес, Олвейз)"),
    ("Основний склад (Інструменти, Барба Італіано)", "Основний склад (Інструменти, Барба Італіано)"),
    ("Склад митниця", "Склад митниця"),
    ("Черкаський офіс (каб. Директорів)", "Черкаський офіс (каб. Директорів)"),
)


class Inventaryzation(models.Model):

    group = models.CharField(max_length=100, choices=INVENT_GROUP, default="---")
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    inv_numb = models.CharField(max_length=15)
    location = models.CharField(max_length=500, choices=LOCATIONS)
    responsible = models.CharField(max_length=200)
    description = models.TextField(default='-', blank=True)
    # price = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.0)
    date_of_purchase = models.DateField(default=None, null=True, blank=True)
    # market_price = models.PositiveIntegerField(default=0) # if do not have price
    market_price = models.FloatField(default=0.0)  # when do not have price
    date_of_registration = models.DateField(default=None, null=True, blank=True)  # when do not have date_of_purchase


class ArchiveUtil(models.Model):

    group = models.CharField(max_length=100)
    name_model = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    inv_numb = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    reason_for_disposal = models.TextField()
    date_of_registration = models.DateField()
    date_of_utilization = models.DateField(default=date.today)


class Act(models.Model):

    operation = models.CharField(max_length=100)
    file = models.FileField(upload_to='acts')
    data_create = models.DateField(default=date.today)

    def __str__(self):
        return str(self.file).split('/')[-1]


class Jurnal(models.Model):

    autor = models.CharField(max_length=100, default='-') # фиксировать юзера под которым делалось действие
    operation = models.CharField(max_length=100, choices=OPERATIONS)
    from_whom = models.CharField(max_length=100)
    to_whom = models.CharField(max_length=100)
    item = models.JSONField()
    reason = models.TextField()
    date_operation = models.DateTimeField(default=datetime.now)
    act_id = models.ForeignKey(Act, on_delete=models.DO_NOTHING, default=None, null=True, blank=True)


class InventarNumberTemp(models.Model):

    number = models.CharField(max_length=15)

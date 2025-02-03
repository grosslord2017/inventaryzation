from django import forms
from django.forms import TextInput
from .models import Inventaryzation
from django.forms.widgets import Textarea, SelectDateWidget, NumberInput, Select
from datetime import date


# Inventaryzation
class InventaryzationAddForm(forms.ModelForm):

    class Meta:
        model = Inventaryzation
        fields = ("group", "name", "model", "serial", "inv_numb", "location", "responsible", "description", "price",
                  "date_of_purchase", "market_price", "date_of_registration")
        widgets = {
            "group": Select,
            "name": TextInput(attrs={"placeholder": "Назва об`єкту"}),
            "model": TextInput(attrs={"placeholder": "Модель об`экту"}),
            "serial": TextInput(attrs={"placeholder": "Серійний номер або VIN номер(якщо це авто)"}),
            "inv_numb": TextInput(attrs={"placeholder": "Інвентарний номер"}),
            #"location": TextInput(attrs={"placeholder": "Адреса"}),
            "location": Select,
            "responsible": TextInput(attrs={"placeholder": "Прізвище, Ім`я, По батькові"}),
            "description": Textarea(attrs={"cols": 50, "rows": 3, "class": "form-control", "placeholder": "Опис"}),
            "price": NumberInput,
            "date_of_purchase":  SelectDateWidget(years=[x for x in range(date.today().year - 10, date.today().year + 1)]),
            "market_price": NumberInput,
            "date_of_registration":  SelectDateWidget(years=[x for x in range(date.today().year - 10, date.today().year + 1)])
        }

        labels = {
            "group": "Група матеріального активу",
            "name": "Назва матеріального активу",
            "model": "Модель",
            "serial": "Серійний номер/VIN-номер для авто",
            "inv_numb": "Інвентарний номер",
            "location": "Місцезнаходження нематеріального активу",
            "responsible": "Матеріально-відповідальна особа",
            "description": "Опис",
            "price": "Ціна придбання, з ПДВ (грн.)",
            "date_of_purchase": "Дата придбання",
            "market_price": "Ринкова ціна на момент постановки на облік, якщо ціна придбання невідома (грн)",
            "date_of_registration": "Дата оприбуткування, якщо дата придбання невідома"
        }
from django import forms
from .models import Worker, Item, Location
from django.forms.widgets import Textarea, SelectDateWidget, SelectMultiple, NumberInput


# class UserLoginForm(forms.Form):
#
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class AddNewItem(forms.ModelForm):

    class Meta:
        model = Item
        fields = ("name", "model", "serial", "description", "worker", "date_of_purchase", "price", "is_reserve")
        widgets = {
            "description": Textarea(attrs={"cols": 50, "rows": 5}),
            "worker": SelectMultiple,
            "date_of_purchase": SelectDateWidget,
            "price": NumberInput
        }


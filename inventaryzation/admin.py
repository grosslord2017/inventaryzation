from django.contrib import admin
from .models import Inventaryzation


# Register your models here.

class InventaryzationAdmin(admin.ModelAdmin):

    list_display = ('group', 'name', 'model', 'serial', 'location', 'responsible', 'description', 'price',
                    'date_of_purchase', 'market_price', 'date_of_registration')
    # list_display_link = ('name', 'model')
    search_fields = ('group', 'name', 'model', 'serial', 'location', 'responsible')
    list_filter = ('group', 'name', 'location', 'responsible', 'date_of_purchase', 'date_of_registration')

admin.site.register(Inventaryzation, InventaryzationAdmin)

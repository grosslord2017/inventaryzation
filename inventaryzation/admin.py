from django.contrib import admin
from .models import Inventaryzation, ArchiveUtil, Jurnal, Act


# Register your models here.

class InventaryzationAdmin(admin.ModelAdmin):

    list_display = ('group', 'name', 'model', 'serial', 'location', 'responsible', 'description', 'price',
                    'date_of_purchase', 'market_price', 'date_of_registration')
    # list_display_link = ('name', 'model')
    search_fields = ('group', 'name', 'model', 'serial', 'location', 'responsible')
    list_filter = ('group', 'name', 'location', 'responsible', 'date_of_purchase', 'date_of_registration')


class ArchiveUtilAdmin(admin.ModelAdmin):

    list_display = ('group', 'name_model', 'serial', 'inv_numb', 'responsible', 'description', 'price',
                    'reason_for_disposal', 'date_of_registration', 'date_of_utilization')
    search_fields = ('group', 'name_model', 'serial', 'inv_numb', 'responsible')
    list_filter = ('group', 'responsible', 'date_of_registration', 'date_of_utilization')


class JurnalAdmin(admin.ModelAdmin):

    list_display = ('operation', 'from_whom', 'to_whom', 'item', 'reason', 'date_operation', 'act_id')
    search_fields = ('operation', 'from_whom', 'to_whom', 'item', 'reason', 'date_operation', 'act_id')
    list_filter = ('operation', 'from_whom', 'to_whom', 'reason', 'act_id')
    list_display_link = ('act_id',)


class ActAdmin(admin.ModelAdmin):

    list_display = ('operation', 'file', 'data_create')
    search_fields = ('operation', 'file', 'data_create')
    list_filter = ('operation', 'file', 'data_create')


admin.site.register(Inventaryzation, InventaryzationAdmin)
admin.site.register(ArchiveUtil, ArchiveUtilAdmin)
admin.site.register(Jurnal, JurnalAdmin)
admin.site.register(Act, ActAdmin)

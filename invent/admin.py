from django.contrib import admin
from .models import Item, Worker, Location


# Register your models here.

class LocationAdmin(admin.ModelAdmin):

    list_display = ('city', 'name', 'address')
    list_display_links = ('city', 'name', 'address')
    search_fields = ('city', 'name')

class WorkerAdmin(admin.ModelAdmin):

    list_display = ('name', 'surname', 'job_position', 'location')
    list_display_link = ('name', 'surname', 'job_position', 'location')
    search_fields = ('name', 'surname', 'job_position', 'location')
    list_filter = ('name', 'surname', 'job_position', 'location')


    # if we delete workers and item dont have workers in final - item move in reserve.
    def delete_queryset(self, request, queryset):
        for qty in queryset:
            items = Item.objects.filter(worker__id=int(qty.id))

            if items:
                if len(items[0].worker.all()) <= 1:
                    for item in items:
                        item.is_reserve = True
                        item.save()

            super().delete_queryset(request, qty)

        self.message_user(request, f'{queryset} has been deleted success!')


class ItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'model', 'serial', 'description', 'date_of_purchase', 'price', 'is_reserve',
                    'is_decommissioned')


admin.site.register(Location, LocationAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Item, ItemAdmin)

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inventaryzation, name='inventaryzation'),
    path('inv_add_new_item', views.inv_add_new_item, name='inv_add_new_item'),
    path('download', views.download, name='download'),
    path('search', views.search, name='search'),
    path('filter_location', views.filter_location, name='filter_location'),
    path('filter_group', views.filter_group, name='filter_group'),
    path('filter_date', views.filter_date, name='filter_date'),
    path('filter_price', views.filter_price, name='filter_price'),
    path('quantity_barcode', views.quantity_barcode, name='quantity_barcode'),
    path('generate_inventar_number', views.generate_inventar_number, name='generate_inventar_number'),
    path('change_responsible', views.change_responsible, name='change_responsible'),
    path('utilization', views.utilization, name='utilization'),
    path('items_in_responsible', views.items_in_responsible, name='items_in_responsible'),
    path('all_acts', views.all_acts, name='all_acts'),
    path('jurnal', views.jurnal, name='jurnal')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
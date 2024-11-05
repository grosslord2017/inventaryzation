from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('items/<pk>/', views.items_list, name='items_list'),
    path('worker_item/<int:pk>', views.worker_items_list, name='worker_items_list'),
    path('adding_new_item', views.add_new_item, name='adding'),
    path('moving', views.moving_item, name='moving'),
    path('history', views.history, name='history'),

    path('ajax_location_workers/', views.ajax_location_workers, name='ajax_location_workers'),
    path('ajax_worker_items/', views.ajax_worker_items, name='ajax_worker_items'),
    path('ajax_decommissioned/', views.ajax_decommissioned, name='ajax_decommissioned'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inventaryzation, name='inventaryzation'),
    path('inv_add_new_item', views.inv_add_new_item, name='inv_add_new_item'),
    path('download', views.download, name='download'),
    #path('upload', views.upload, name='upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
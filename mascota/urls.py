from django.urls import path
from mascota.views import *

urlpatterns = [
    path('', mascota, name='mascota'),
    path('nuevo/', mascotaView, name='mascotaView'),
    path('lista/', mascota_list, name='mascota_list'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_edit'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name='mascota_delete'),
]
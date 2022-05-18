from django.urls import path
from mascota.views import *

urlpatterns = [
    path('', mascota, name='mascota'),
    path('nuevo/', MascotaCreate.as_view(), name='mascotaView'),
    path('lista/', MascotaList.as_view(), name='mascota_list'),
    path('editar/<pk>/', MascotaUpdate.as_view(), name='mascota_edit'),
    path('eliminar/<pk>/', MascotaDelete.as_view(), name='mascota_delete'),
]
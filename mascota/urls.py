from django.urls import path
from django.contrib.auth.decorators import login_required
from mascota.views import *

urlpatterns = [
    path('', mascota, name='mascota'),
    path('home/', home, name='home'),
    path('nuevo/', login_required(MascotaCreate.as_view()), name='mascotaView'),
    path('lista/', login_required(MascotaList.as_view()), name='mascota_list'),
    path('editar/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_edit'),
    path('eliminar/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_delete'),
    path('listado', listado, name='listado'),
]
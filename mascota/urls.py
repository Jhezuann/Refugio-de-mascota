from django.urls import path
from mascota.views import mascota, mascotaView

urlpatterns = [
    path('', mascota, name='mascota'),
    path('nuevo/', mascotaView, name='mascotaView'),
]

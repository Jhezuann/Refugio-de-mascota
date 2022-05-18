from django.urls import path
from adopcion.views import *

urlpatterns = [
	path('', index),
	path('solicitud/listar', SolicitudList.as_view(), name='SolicitudList'),
	path('solicitud/nueva', SolicitudCreate.as_view(), name='SolicitudCreate'),
]

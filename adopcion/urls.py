from django.urls import path
from adopcion.views import *

urlpatterns = [
	path('', index),
	path('solicitud/listar', SolicitudList.as_view(), name='SolicitudList'),
	path('solicitud/nueva', SolicitudCreate.as_view(), name='SolicitudCreate'),
	path('solicitud/editar/<pk>/', SolicitudUpdate.as_view(), name='SolicitudUpdate'),
	path('solicitud/eliminar/<pk>/', SolicitudDelete.as_view(), name='SolicitudDelete'),
]

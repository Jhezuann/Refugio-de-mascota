from django.urls import path
from usuario.views import *

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name='RegistroUsuario'),
    path('api/', UserAPI.as_view(), name='api'),
]
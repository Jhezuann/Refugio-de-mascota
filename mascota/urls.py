from django.urls import path
from mascota.views import index

urlpatterns = [
    path('', index),
]

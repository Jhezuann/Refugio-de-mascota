from django.urls import path
from adopcion.views import index

urlpatterns = [
	path('', index),
]

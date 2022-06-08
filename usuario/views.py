from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import *
from django.urls import reverse_lazy
from usuario.forms import *
from rest_framework.views import *
from usuario.serializers import UserSerializer
import json

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registrar.html'
    form_class= RegistroForm
    success_url = reverse_lazy('home')

class UserAPI(APIView):
    serializer=UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return Response(json.dumps(response.data), content_type='application/json')
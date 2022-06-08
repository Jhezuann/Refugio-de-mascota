from django.shortcuts import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import *
from mascota.forms import MascotaForm
from mascota.models import *
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.
def listado(request):
	lista=serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def mascota(request):
	return render(request, 'mascota.html')

def home(request):
	return render(request, 'home.html')

class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota_list.html'
	context_object_name = 'mascotas'
	paginate_by=5

class MascotaCreate(CreateView):
	model=Mascota
	form_class=MascotaForm
	template_name= 'mascota_form.html'
	success_url=reverse_lazy('mascota_list')

class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota_form.html'
	success_url = reverse_lazy('mascota_list')

class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota_delete.html'
	success_url = reverse_lazy('mascota_list')


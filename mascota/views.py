from django.shortcuts import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import *
from mascota.forms import MascotaForm
from mascota.models import *

# Create your views here.

def mascota(request):
	return render(request, 'mascota.html')

class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota_list.html'
	context_object_name = 'mascotas'

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
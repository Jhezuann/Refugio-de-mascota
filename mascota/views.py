from django.shortcuts import render, redirect
from django.http import HttpResponse
from mascota.forms import MascotaForm

# Create your views here.

def mascota(request):
	return render(request, 'mascota.html')

def mascotaView(request):
	if request.method=='POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota')
	else:
		form =MascotaForm()
	return render(request, 'mascota_form.html', {'form':form})
from django import forms
from mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model=Mascota

		fields=[
			'nombre',
			'sexo',
			'edadAproximada',
			'fechaDeRescate',
			'persona',
			'vacuna',
		]
		labels= {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edadAproximada': 'Edad aproximada',
			'fechaDeRescate': 'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}
		widgets={
			'nombre': forms.TextInput(attrs={'class':'form.control'}),
			'sexo': forms.TextInput(attrs={'class':'form.control'}),
			'edadAproximada': forms.TextInput(attrs={'class':'form.control'}),
			'fechaDeRescate': forms.TextInput(attrs={'class':'form.control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}
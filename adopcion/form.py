from pyexpat import model
from django import forms
from adopcion.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio'
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'telefono':'Telefono',
            'email':'Email',
            'domicilio':'Domicilio'
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.Textarea(attrs={'class':'form-control'})
        }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields=[
            'numero_mascota',
            'razones'
        ]
        labels={
            'numero_mascota':'Numero de Mascota',
            'razones':'Razones para adoptar'
        }
        widgets={
            'numero_mascota':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'})
        }
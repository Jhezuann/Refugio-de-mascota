from django.db import models
from adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
	nombre=models.CharField(max_length=50)

class Mascota(models.Model):
	nombre=models.CharField(max_length=50)
	sexo=models.CharField(max_length=10)
	edadAproximada=models.IntegerField()
	fechaDeRescate=models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)
	
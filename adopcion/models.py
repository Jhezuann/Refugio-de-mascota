from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=30)
	email = models.EmailField()
	domicilio=models.TextField()

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

class Solicitud(models.Model):
	persona=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	numero_mascota=models.IntegerField()
	razones=models.TextField()
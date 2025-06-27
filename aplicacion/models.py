from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class PerfilPaciente(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    obra_social = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    class Meta:
        verbose_name = 'Perfil Paciente'
        verbose_name_plural = 'Perfiles Pacientes'


class historiaclinica(models.Model):
    perfil_paciente = models.ForeignKey(PerfilPaciente, on_delete=models.CASCADE, null=True, related_name="historiaclinica_set")
    motivo_consulta = models.TextField(blank=True, null=True)
    antecedentes = models.TextField(blank=True, null=True)
    diagnostico = models.CharField(max_length=50, blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    fecha_consulta = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(null=True, blank=True)
    seguimiento = models.TextField(blank=True, null=True)
    evaluacion = models.TextField(blank=True, null=True)
    estudios_complementarios = models.TextField(blank=True, null=True)
    archivos = models.FileField(upload_to='archivos/', blank=True, null=True)

    def __str__(self):
        return f"Historia Clínica de {self.perfil_paciente.nombre} {self.perfil_paciente.apellido}"
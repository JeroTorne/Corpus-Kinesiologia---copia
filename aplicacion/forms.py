from django import forms
from .models import *



class PacienteForm(forms.ModelForm):
    class Meta:
        model = PerfilPaciente
        fields = ['nombre', 'apellido', 'dni', 'ocupacion', 'telefono', 'fecha_nacimiento', 'edad','obra_social']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ocupación'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+549) 11 1234-5678', 'type': 'tel'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Nacimiento', 'type': 'date'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'obra_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obra Social'}),
        }

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = historiaclinica
        fields = [
            'perfil_paciente', 
            'motivo_consulta', 
            'antecedentes', 
            'diagnostico', 
            'tratamiento',
            'seguimiento',
            'evaluacion',
            'estudios_complementarios',
            'archivos',
        ]  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['perfil_paciente'].widget.attrs['readonly'] = True
        self.fields['perfil_paciente'].widget.attrs['class'] = 'form-control'
        self.fields['perfil_paciente'].widget.attrs['placeholder'] = 'Paciente'
        # Agregar atributos para el campo de archivo
        self.fields['archivos'].widget.attrs.update({
            'class': 'form-control',
            'accept': '.pdf,.doc,.docx,.jpg,.jpeg,.png,.flv,.mp4'  # Tipos de archivo permitidos
        })






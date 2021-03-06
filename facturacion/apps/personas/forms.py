from django import forms
from apps.personas.models import Persona
from datetime import datetime

YEARS = sorted(list(range(1950, datetime.now().year)), reverse=True)
# MONTHS = {
#     1: _('Enero'), 2: _('Febrero'), 3: _('Marzo'), 4: _('Abril'),
#     5: _('Mayo'), 6: _('Junio'), 7: _('Julio'), 8: _('Agosto'),
#     9: _('Septiembre'), 10: _('Octubre'), 11: _('Noviembre'), 12: _('Diciembre')
# }


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'primer_apellido',
            'segundo_apellido',
            'tipo_identificacion',
            'identificacion',
            'genero',
            'email',
            'telefono',
            'direccion',
            'nacimiento',
            'rol',
        ]
        labels = {
            'nombres': 'Nombres',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'tipo_identificacion': 'Tipo de Identificación',
            'identificacion': 'Número de Identificación',
            'genero': 'Género',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'nacimiento': 'Fecha de Nacimiento',
            'rol': 'Rol',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_identificacion': forms.Select(attrs={'class': 'form-control'}),
            'identificacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nacimiento': forms.SelectDateWidget(years=YEARS, attrs={'class': 'form-control'}),
            'rol': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

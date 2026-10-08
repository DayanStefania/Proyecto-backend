from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nombre_mascota',
            'tipo_mascota',
            'nombre_dueno',
            'telefono',
            'correo',
            'fecha_entrada',
            'fecha_salida',
            'servicio',
            'observaciones',
            'precio',
        ]

        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')

        if precio is not None and precio <= 0:
            raise forms.ValidationError(
                'El precio debe ser mayor que cero.'
            )

        return precio

    def clean(self):
        cleaned_data = super().clean()

        fecha_entrada = cleaned_data.get('fecha_entrada')
        fecha_salida = cleaned_data.get('fecha_salida')

        if fecha_entrada and fecha_salida:
            if fecha_salida < fecha_entrada:
                self.add_error(
                    'fecha_salida',
                    'La fecha de salida no puede ser anterior a la fecha de entrada.'
                )

        return cleaned_data
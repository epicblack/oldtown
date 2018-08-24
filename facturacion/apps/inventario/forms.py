from django import forms
from apps.inventario.models import Producto, Servicio


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'presentacion',
            'unidad',
            'precio_compra',
            'precio_venta',
            'cantidad',
        ]
        labels = {
            'nombre': 'Nombre del Artículo',
            'descripcion': 'Descripción',
            'presentacion': 'Presentación',
            'unidad': 'Unidad',
            'precio_compra': 'Precio de Compra',
            'precio_venta': 'Precio de Venta',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'presentacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre',
            'descripcion',
            'precio_venta',
        ]
        labels = {
            'nombre': 'Nombre del Servicio',
            'descripcion': 'Descripción',
            'precio_venta': 'Precio de Venta',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
        }

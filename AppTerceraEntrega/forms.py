from django import forms

class EmpleadoFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.CharField(required=True)
    celular = forms.IntegerField(required=True)
    
class ProductosNuevosFormulario(forms.Form):
    
    marca = forms.CharField(required=True)
    version = forms.CharField(required=True)
    largo = forms.IntegerField(required=True)
    
class ProductosUsadosFormulario(forms.Form):
    
    marca = forms.CharField(required=True)
    version = forms.CharField(required=True)
    largo = forms.IntegerField(required=True)
    
class EquipamientosFormulario(forms.Form):
    
    Nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=True)
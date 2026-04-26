from django import forms

class ServicioForm(forms.Form):
    categoria = forms.CharField(label='ID de Categoría (Oculto)', widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    titulo = forms.CharField(max_length=50, min_length=3, label='Título del Servicio', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), min_length=10, label='Descripción')
    url = forms.CharField(required=False, label='URL de destino', widget=forms.TextInput(attrs={'class': 'form-control'}))
    icono = forms.URLField(required=False, label='URL del Ícono', widget=forms.URLInput(attrs={'class': 'form-control'}))

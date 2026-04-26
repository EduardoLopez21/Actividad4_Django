from django.shortcuts import render, redirect
from django import forms
from django.utils.text import slugify
import time
import json

class ServicioForm(forms.Form):
    def __init__(self, *args, **kwargs):
        dynamic_categories = kwargs.pop('dynamic_categories', [])
        super(ServicioForm, self).__init__(*args, **kwargs)
        
        CATEGORIAS_BASE = [
            ('inicio', 'Inicio (Servicios Principales)'),
            ('dsf', 'Desarrollo de Software'),
            ('adb', 'Administración de Bases de Datos'),
            ('gr', 'Gestión de Redes'),
            ('ia', 'Inteligencia Artificial')
        ]
        
        for cat in dynamic_categories:
            CATEGORIAS_BASE.append((cat['slug'], cat['titulo']))
            
        self.fields['categoria'] = forms.ChoiceField(
            choices=CATEGORIAS_BASE, 
            required=True, 
            label="Categoría",
            error_messages={'required': 'Debes seleccionar una categoría.'}
        )

    
    titulo = forms.CharField(
        max_length=50, 
        min_length=3, 
        required=True,
        error_messages={
            'required': 'El título es obligatorio.',
            'min_length': 'El título debe tener al menos 3 caracteres.',
            'max_length': 'El título no puede exceder los 50 caracteres.'
        }
    )
    descripcion = forms.CharField(
        max_length=200, 
        min_length=10, 
        required=True,
        widget=forms.Textarea,
        error_messages={
            'required': 'La descripción es obligatoria.',
            'min_length': 'La descripción debe tener al menos 10 caracteres.',
            'max_length': 'La descripción no puede exceder los 200 caracteres.'
        }
    )
    url = forms.CharField(
        max_length=100, 
        required=False,
        initial='#',
        error_messages={
            'max_length': 'La URL no puede exceder los 100 caracteres.'
        }
    )
    icono = forms.URLField(
        required=False,
        error_messages={
            'invalid': 'Por favor ingresa una URL de imagen válida.'
        }
    )

def inicio(request):
    nuevos_servicios = request.session.get('nuevos_inicio', [])
    # Filter out dynamically created IA service since it's now hardcoded
    nuevos_servicios = [s for s in nuevos_servicios if s.get('titulo', '').strip().lower() != 'inteligencia artificial']
    request.session['nuevos_inicio'] = nuevos_servicios
    
    old_servicios = request.session.get('nuevos_servicios', [])
    old_servicios = [s for s in old_servicios if s.get('titulo', '').strip().lower() != 'inteligencia artificial']
    request.session['nuevos_servicios'] = old_servicios
    
    context = {
        'now': int(time.time()),
        'nuevos_servicios_json': json.dumps(old_servicios + nuevos_servicios)
    }
    return render(request, 'plantilla.html', context)

def agregar_servicio(request):
    nuevos_inicio = request.session.get('nuevos_inicio', [])
    dynamic_categories = [{'slug': item.get('slug', slugify(item['titulo'])), 'titulo': item['titulo']} for item in nuevos_inicio]

    if request.method == 'POST':
        form = ServicioForm(request.POST, dynamic_categories=dynamic_categories)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            
            if categoria == 'inicio':
                slug = slugify(form.cleaned_data['titulo'])
                url = f'/servicio/{slug}/'
            else:
                slug = None
                url = form.cleaned_data.get('url')
                if not url:
                    url = '#'

            nuevo_servicio = {
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'url': url
            }
            if slug:
                nuevo_servicio['slug'] = slug

            if form.cleaned_data['icono']:
                nuevo_servicio['icono'] = form.cleaned_data['icono']

            session_key = f'nuevos_{categoria}'
            servicios = request.session.get(session_key, [])
            servicios.append(nuevo_servicio)
            request.session[session_key] = servicios
            
            if categoria == 'inicio':
                return redirect('inicio')
            if categoria == 'dsf':
                return redirect('dsf')
            if categoria == 'adb':
                return redirect('adb')
            if categoria == 'gr':
                return redirect('gr')
            if categoria == 'ia':
                return redirect('ia')
                
            return redirect('servicio_dinamico', slug=categoria)
    else:
        cat = request.GET.get('cat', 'inicio')
        form = ServicioForm(initial={'url': '#', 'categoria': cat}, dynamic_categories=dynamic_categories)

    return render(request, 'agregar.html', {'form': form, 'now': int(time.time())})

def dsf(request):
    nuevos = request.session.get('nuevos_dsf', [])
    return render(request, 'dsf.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def adb(request):
    nuevos = request.session.get('nuevos_adb', [])
    return render(request, 'adb.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def gr(request):
    nuevos = request.session.get('nuevos_gr', [])
    return render(request, 'gr.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def ia(request):
    nuevos = request.session.get('nuevos_ia', [])
    return render(request, 'ia.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def servicio_dinamico(request, slug):
    nuevos_inicio = request.session.get('nuevos_inicio', [])
    servicio_actual = next((item for item in nuevos_inicio if item.get('slug') == slug), None)
    
    if not servicio_actual:
        return redirect('inicio')
        
    session_key = f'nuevos_{slug}'
    nuevos = request.session.get(session_key, [])
    
    context = {
        'now': int(time.time()),
        'servicio': servicio_actual,
        'nuevos_json': json.dumps(nuevos),
        'slug': slug
    }
    return render(request, 'servicio_dinamico.html', context)
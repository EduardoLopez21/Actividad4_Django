import json
import time
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ServicioForm
from .models import Servicio

def get_nuevos_servicios(categoria):
    servicios = Servicio.objects.filter(categoria=categoria)
    return [{'titulo': s.titulo, 'descripcion': s.descripcion, 'url': s.url, 'icono': s.icono, 'id': s.id} for s in servicios]

def inicio(request):
    nuevos = get_nuevos_servicios('inicio')
    return render(request, 'plantilla.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def dsf(request):
    nuevos = get_nuevos_servicios('dsf')
    return render(request, 'dsf.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def adb(request):
    nuevos = get_nuevos_servicios('adb')
    return render(request, 'adb.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def gr(request):
    nuevos = get_nuevos_servicios('gr')
    return render(request, 'gr.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def ia(request):
    nuevos = get_nuevos_servicios('ia')
    return render(request, 'ia.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def agregar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            nuevo_servicio = Servicio(
                categoria=form.cleaned_data['categoria'],
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion'],
                url=form.cleaned_data['url'],
                icono=form.cleaned_data['icono'] or ''
            )
            nuevo_servicio.save()
            
            categoria = nuevo_servicio.categoria
            if categoria in ['inicio', 'dsf', 'adb', 'gr', 'ia']:
                return redirect(categoria)
            else:
                return redirect('servicio_dinamico', slug=categoria)
    else:
        initial_cat = request.GET.get('cat', 'inicio')
        form = ServicioForm(initial={'categoria': initial_cat})

    return render(request, 'agregar.html', {'form': form, 'now': int(time.time())})

def eliminar_servicio(request):
    categoria = request.GET.get('cat')
    index = request.GET.get('idx')
    if categoria and index is not None:
        try:
            index = int(index)
            # Find the service at the given index in the category
            servicios = list(Servicio.objects.filter(categoria=categoria).order_by('id'))
            if 0 <= index < len(servicios):
                servicios[index].delete()
        except ValueError:
            pass
            
    if categoria in ['inicio', 'dsf', 'adb', 'gr', 'ia']:
        return redirect(categoria)
    elif categoria:
        return redirect('servicio_dinamico', slug=categoria)
    return redirect('inicio')

def notas(request):
    return render(request, 'notas.html')

def servicio_dinamico(request, slug):
    nuevos = get_nuevos_servicios(slug)
    servicio_info = {
        'titulo': slug.replace('-', ' ').title(),
        'descripcion': f'Información sobre {slug.replace("-", " ")}'
    }
    return render(request, 'servicio_dinamico.html', {
        'now': int(time.time()),
        'servicio': servicio_info,
        'slug': slug,
        'nuevos_json': json.dumps(nuevos)
    })
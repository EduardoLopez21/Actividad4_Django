import json
import time
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ServicioForm

def get_nuevos_servicios(request, categoria):
    servicios = request.session.get('nuevos_servicios', {})
    return servicios.get(categoria, [])

def inicio(request):
    nuevos = get_nuevos_servicios(request, 'inicio')
    return render(request, 'plantilla.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def dsf(request):
    nuevos = get_nuevos_servicios(request, 'dsf')
    return render(request, 'dsf.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def adb(request):
    nuevos = get_nuevos_servicios(request, 'adb')
    return render(request, 'adb.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def gr(request):
    nuevos = get_nuevos_servicios(request, 'gr')
    return render(request, 'gr.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def ia(request):
    nuevos = get_nuevos_servicios(request, 'ia')
    return render(request, 'ia.html', {'now': int(time.time()), 'nuevos_json': json.dumps(nuevos)})

def agregar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data['categoria']
            url = form.cleaned_data['url']
            if categoria == 'inicio' and (not url or url == '#'):
                from django.utils.text import slugify
                slug = slugify(form.cleaned_data['titulo'])
                url = reverse('servicio_dinamico', args=[slug])
            elif not url:
                url = '#'

            nuevo_servicio = {
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'url': url,
                'icono': form.cleaned_data['icono'] or '',
            }
            
            servicios_dict = request.session.get('nuevos_servicios', {})
            if categoria not in servicios_dict:
                servicios_dict[categoria] = []
            
            servicios_dict[categoria].append(nuevo_servicio)
            request.session['nuevos_servicios'] = servicios_dict
            request.session.modified = True
            
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
            servicios_dict = request.session.get('nuevos_servicios', {})
            if categoria in servicios_dict and 0 <= index < len(servicios_dict[categoria]):
                servicios_dict[categoria].pop(index)
                if not servicios_dict[categoria]:
                    del servicios_dict[categoria]
                request.session['nuevos_servicios'] = servicios_dict
                request.session.modified = True
        except ValueError:
            pass
            
    if categoria in ['inicio', 'dsf', 'adb', 'gr', 'ia']:
        return redirect(categoria)
    elif categoria:
        return redirect('servicio_dinamico', slug=categoria)
    return redirect('inicio')

def servicio_dinamico(request, slug):
    nuevos = get_nuevos_servicios(request, slug)
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
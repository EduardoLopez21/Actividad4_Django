from django.shortcuts import render

# Create your views here.

import time

def inicio(request):
    return render(request, 'plantilla.html', {'now': int(time.time())})

def dsf(request):
    return render(request, 'dsf.html', {'now': int(time.time())})

def adb(request):
    return render(request, 'adb.html', {'now': int(time.time())})

def gr(request):
    return render(request, 'gr.html', {'now': int(time.time())})
from django.db import models
from django.utils.text import slugify

class Servicio(models.Model):
    CATEGORIA_CHOICES = [
        ('inicio', 'Inicio'),
        ('dsf', 'Desarrollo de Software'),
        ('adb', 'Administración de Bases de Datos'),
        ('gr', 'Gestión de Redes'),
        ('ia', 'Inteligencia Artificial'),
    ]

    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='inicio')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.CharField(max_length=200, blank=True, default='#')
    icono = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
        if self.categoria == 'inicio' and (not self.url or self.url == '#'):
            from django.urls import reverse
            slug = slugify(self.titulo)
            self.url = reverse('servicio_dinamico', args=[slug])
        elif not self.url:
            self.url = '#'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} ({self.categoria})"

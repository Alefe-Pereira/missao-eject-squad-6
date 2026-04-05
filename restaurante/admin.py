from django.contrib import admin
from .models import Reserva, ArtigoBlog, Destaque

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'hora', 'numero_pessoas', 'criado_em']
    list_filter = ['data']
    search_fields = ['nome', 'email']

@admin.register(ArtigoBlog)
class ArtigoBlogAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_publicacao']
    list_filter = ['data_publicacao']
    search_fields = ['titulo']

@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ordem']
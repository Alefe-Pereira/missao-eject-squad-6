from django.contrib import admin
from .models import Reserva, ArtigoBlog, Destaque, Funcionario

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'hora', 'numero_pessoas', 'criado_em']
    list_filter = ['data']
    search_fields = ['nome']

@admin.register(ArtigoBlog)
class ArtigoBlogAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_publicacao', 'autor']
    list_filter = ['data_publicacao']
    search_fields = ['titulo']

@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ordem']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display =  ("usuario", "cargo")
    search_fields = ("usuario__username", "usuario__email")
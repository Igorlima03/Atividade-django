from django.contrib import admin
from clube.models  import Clube
from .models import Jogadore
from .models import Competicoe
from .models import Titulo
from django.utils.html import format_html
@admin.register(Clube)

class ClubeAdmin(admin.ModelAdmin):
    def imagem(self,obj):
        return format_html(f'<img src="{obj.image.url}" width="60"; heigth="60" />')
    list_display = ('nome', 'imagem', 'ano_fundacao', 'divisao','sexo')
    list_filter = ('nome', 'ano_fundacao')
    search_fields = ('nome', 'divisao')
 


@admin.register(Jogadore)
class JogadoreAdmin(admin.ModelAdmin):
    def imagem(self,obj):
        return format_html(f'<img src="{obj.image.url}" width="120"; heigth="60" />')
    list_display = ('nome', 'imagem', 'clube','posicao','numero','sexo')
    search_fields = ('nome', 'clube', 'posicao')


@admin.register(Competicoe)
class competicaoAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'estadual', 'nacional',  'internacional')

@admin.register(Titulo)
class titulosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_titulo', 'ano_conquista', 'data_exata')
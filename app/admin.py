from django.contrib import admin
from .models import *


class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 6

class QuartoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]
    list_display = ('numero', 'alojamento', 'capacidade', 'listar_pessoas')
    search_fields = ('numero', 'alojamento__nome', 'pessoas__nome')
    
    def listar_pessoas(self, obj):
        return ", ".join([pessoa.nome for pessoa in obj.pessoas.all()])
    
    listar_pessoas.short_description = 'Pessoas no Quarto'


admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Pessoa)
admin.site.register(Alojamento)
admin.site.register(Cidade)
admin.site.register(Quarto, QuartoAdmin)
from django.contrib import admin
from core.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
        list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
        list_display_links = ('id', 'nome')
        search_fields = ('nome',)
        list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'nome')
    list_display_links = ('nome', 'codigo_curso')
    search_fields = ('codigo_curso', 'nome')

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
        list_display = ('id', 'aluno', 'curso', 'periodo')
        list_display_links = ('id',)
        
admin.site.register(Matricula, Matriculas)

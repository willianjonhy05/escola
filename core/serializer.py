from rest_framework import serializers
from core.models import Aluno, Curso, Matricula
from django.urls import reverse

class AlunoSerializer(serializers.ModelSerializer):
    perfil_do_aluno = serializers.SerializerMethodField()

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'sexo', 'rg', 'cpf', 'data_nascimento', 'idade', 'perfil_do_aluno']

    def get_perfil_do_aluno(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(reverse('alunos-detail', kwargs={'pk': obj.pk}))
        return None


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    curso = serializers.ReadOnlyField(source='curso.nome')
    periodo = serializers.SerializerMethodField()


    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']


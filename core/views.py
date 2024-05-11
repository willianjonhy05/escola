from rest_framework import viewsets, generics
from core.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

class AlunosViewSet(viewsets.ModelViewSet):    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
        """Listando todas as matrículas"""
        queryset = Matricula.objects.all()
        serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    serializer_class = ListaMatriculasAlunoSerializer
    def get_queryset(self):
        id_aluno = self.kwargs['pk']
        queryset = Matricula.objects.filter(aluno_id=id_aluno)
        return queryset
    

class ListaAlunosMatriculados(generics.ListAPIView):    
    def get_queryset(self):
        id_do_curso = self.kwargs['pk']
        queryset = Matricula.objects.filter(curso_id=id_do_curso)
        return queryset

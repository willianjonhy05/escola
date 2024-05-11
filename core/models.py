from datetime import date

from django.db import models

class Aluno(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)  
    
    @property
    def idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nascimento
        return round(diferenca.days // 365.25)  

    def __str__(self):
        return self.nome 
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    nome = models.CharField(max_length=100)
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, 
	    null=False,default='B')
    
    def __str__(self):
        return self.nome



class Matricula(models.Model):
        PERIODO = (
                ('M', 'Matutino'),
                ('V', 'Vespertino'),
                ('N', 'Noturno')
        )
        aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

    

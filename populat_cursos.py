import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escola.settings')
django.setup()


from faker import Faker
import random
from core.models import Curso

def criar_cursos(quantidade):
    fake = Faker('pt_BR')
    niveis = ['B', 'I', 'A']
    for _ in range(quantidade):
        nome = fake.text(max_nb_chars=30)
        codigo_curso = fake.unique.lexify(text='???-###')  # Gera um código único de 3 letras seguido de 3 números
        descricao = fake.text(max_nb_chars=100)
        nivel = random.choice(niveis)
        curso = Curso.objects.create(nome=nome, codigo_curso=codigo_curso, descricao=descricao, nivel=nivel)
        curso.save()

criar_cursos(15)
print("Cursos gerados com sucesso!")
import os
import django

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE manualmente para garantir que o Django saiba onde encontrar as configurações.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escola.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from core.models import Aluno

def criando_alunos(quantidade_de_pessoas):
    Faker.seed(5)  # Definindo a semente antes de criar o objeto Faker
    fake = Faker('pt_BR')  # Criando o objeto Faker depois de definir a semente
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=30)
        email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = email.replace(' ', '')  # Remova espaços em branco adicionais
        cpf = cpf.generate()
        sexo = random.choice(['M', 'F'])
        # Modifiquei a geração do RG para evitar zeros à esquerda
        rg = "{:02d}{:03d}{:03d}{:01d}".format(random.randint(10, 99), random.randint(100, 999), random.randint(100, 999), random.randint(0, 9))
        telefone = "{} 9{}-{}".format(random.randint(10, 20), random.randint(4000, 9999), random.randint(4000, 9999))
        p = Aluno(nome=nome, data_nascimento=data_nascimento, rg=rg, cpf=cpf, sexo=sexo, email=email, telefone=telefone)
        p.save()

criando_alunos(50)
print("Sucesso!")

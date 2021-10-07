from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=5)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.matricula, self.nome)


class Chamado(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    telefone = models.CharField(max_length=10)
    data_abertura = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return 'C{} - {}'.format(self.id, self.titulo)


class Atendimento(models.Model):
    descricao = models.TextField()
    atendente = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)

    def __str__(self):
        return 'Atendimento do chamado C{} - {}'.format(self.chamado.id, self.descricao)

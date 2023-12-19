import json

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Modalidade(models.Model):
    nome = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nome

class Liga(models.Model):
    nome = models.CharField(max_length=20 , default="")
    ano = models.DateField()
    fase = models.CharField(max_length=20)
    modalidade = models.ForeignKey('Modalidade', on_delete=models.CASCADE)
    pais = models.CharField(max_length=10)
    equipas = models.ManyToManyField('Equipa', blank=True)

    def __str__(self, modalidade=None):
        return "Liga de " + str(self.pais) + " do ano " + str(self.ano) + " na modalidade " + str(modalidade.nome)

class Grupo(models.Model):
    nome = models.CharField(max_length=10)
    liga = models.ForeignKey('Liga', on_delete=models.CASCADE,   blank=True)

    def __str__(self):
        return "Grupo " + str(self.id_grupo) + " " + self.nome + " " + self.liga

class Equipa(models.Model):
    nome = models.CharField(max_length=50)
    grupos = models.ManyToManyField('Grupo',  blank=True)
    def __str__(self):
        return self.nome

class Jogador(models.Model):
    fullname = models.CharField(max_length=50, blank=True)
    valor = models.DecimalField(max_digits=50, decimal_places=2)
    id_equipa = models.ForeignKey('Equipa', on_delete=models.CASCADE)
    pontos = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return "Jogador " + str(self)

class Jogo(models.Model):
    equipa_casa = models.ForeignKey('Equipa', on_delete=models.CASCADE)
    equipa_fora = models.ForeignKey('Jogador', on_delete=models.CASCADE)
    golos_eq_casa = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(0)])
    golos_eq_fora = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(0)])
    tempo_fim_1p = models.DecimalField(max_digits=4, decimal_places=1)
    tempo_fim_2p = models.DecimalField(max_digits=4, decimal_places=1)
    liga = models.ForeignKey('Liga', on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return "Jogo " + str(self.id_jogo) +" em " + str(self.data) + " da liga " + str(self.liga)

class Evento(models.Model):
    jogador = models.ForeignKey('Jogador', on_delete=models.CASCADE)
    jogo = models.ForeignKey('Jogo', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10)
    tempo = models.CharField(max_length=6)

    def __str__(self):
        return "No jogo " + str(self.jogo) + " o jogador " + str(self.jogador) + " fez " + str(self.tipo) + " no tempo " + str(self.tempo)

class Classificacao(models.Model):
    equipa = models.ForeignKey('Equipa', on_delete=models.CASCADE)
    liga = models.ForeignKey('Liga', on_delete=models.CASCADE)
    nrPontos = models.DecimalField(max_digits=10,decimal_places=1)

    def __str__(self):
        return "Classificacao " + str(self)

class User(models.Model):
    username = models.CharField(max_length=20, blank=True)
    FirstName = models.CharField(max_length=20, blank=True)
    LastName = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, default='<PASSWORD>')
    email = models.EmailField()
    role = models.CharField(max_length=8)
    token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

class FantasyTeam(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    liga = models.ForeignKey('Liga', on_delete=models.CASCADE)
    team_name = models.CharField(max_length=20)
    players = models.ManyToManyField('Jogador')
    capitan = models.CharField(max_length=20, blank=True)


from django.db import models
import arrow

# Create your models here.
from django.utils import timesince
from django.utils.datetime_safe import date


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()

    @property
    def idade(self):
        return timesince.timesince(self.data_nascimento)


    def __unicode__(self):
        return "{0} - {1}".format(self.nome, self.data_nascimento)


class Carro(models.Model):
    marca = models.CharField(max_length=24)
    fabricacao = models.DateField()

    def __unicode__(self):
        return "{1} - {0}".format(self.fabricacao, self.marca)

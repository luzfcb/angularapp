import json
from braces.views import JSONResponseMixin
from django.http import HttpResponse
from .models import Pessoa, Carro
from django.shortcuts import render
from django.db import models
from django import forms
# Create your views here.
from django.views import generic
from rest_framework import routers, serializers, viewsets


class PessoaListView(JSONResponseMixin, generic.ListView):
    model = Pessoa



def pizzas(request):
    response_data = """[{"nome": "Margarita", "tamanho": "gigante", "valor": "42.90", "ingredientes": "Tomate, Cebola, Queijo, Manjeric\u00e3o", "foto": "https://fratelli.s3.amazonaws.com/cache/a9/ef/a9efe9151a9a0fb1ed0b01a694418318.jpg"}, {"nome": "Mussarela", "tamanho": "gigante", "valor": "42.90", "ingredientes": "Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/2b/ec/2bece2cd92d99fc7047b1c238067da83.jpg"}, {"nome": "Calabreza", "tamanho": "gigante", "valor": "42.90", "ingredientes": "Calebreza, Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/e8/5b/e85b83b7fa738934661e8789bcc94bc5.jpg"}, {"nome": "Mussarela", "tamanho": "grande", "valor": "26.90", "ingredientes": "Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/f8/8c/f88cacc7833b0909134f2ed6740db375.jpg"}, {"nome": "Margarita", "tamanho": "grande", "valor": "26.90", "ingredientes": "Tomate, Cebola, Queijo, Manjeric\u00e3o", "foto": "https://fratelli.s3.amazonaws.com/cache/f4/8f/f48fea4d0c9d2bfd2349d4b836eb580a.jpg"}, {"nome": "Calabreza", "tamanho": "grande", "valor": "26.90", "ingredientes": "Calebreza, Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/8c/0c/8c0c65d5de7cb524a44a803b9db343f7.jpg"}, {"nome": "Calabreza", "tamanho": "media", "valor": "16.90", "ingredientes": "Calebreza, Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/8e/f4/8ef4d2b2a4af90baec336c8c14bbd889.jpg"}, {"nome": "Margarita", "tamanho": "media", "valor": "16.90", "ingredientes": "Tomate, Cebola, Queijo, Manjeric\u00e3o", "foto": "https://fratelli.s3.amazonaws.com/cache/53/6e/536ed74d1dc505ed13fc10b5844a0e00.jpg"}, {"nome": "Mussarela", "tamanho": "media", "valor": "16.90", "ingredientes": "Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/4c/67/4c6791d020030965e8a4cdca17bebf46.jpg"}, {"nome": "Margarita", "tamanho": "pequena", "valor": "9.90", "ingredientes": "Tomate, Cebola, Queijo, Manjeric\u00e3o", "foto": "https://fratelli.s3.amazonaws.com/cache/fc/44/fc44e1c95077c6c9172e5077c1a74d8f.jpg"}, {"nome": "Mussarela", "tamanho": "pequena", "valor": "9.90", "ingredientes": "Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/24/31/24318dfd9106cd060f42c7b65dfd1cb0.jpg"}, {"nome": "Calabreza", "tamanho": "pequena", "valor": "9.90", "ingredientes": "Calebreza, Queiro Mussarela, Tomate, Azeitona", "foto": "https://fratelli.s3.amazonaws.com/cache/61/91/619114080c518799ede6afe3caf48f6c.jpg"}]"""
    return HttpResponse(response_data, content_type="application/json")

class F(forms.ModelForm):

    class Meta:
        model = Carro

class Home(generic.CreateView):
    model = Carro
    template_name = 'novo/base.html'
    success_url = '/'




# Serializers define the API representation.
# class PessoaSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pessoa
#         fields = ('nome', 'data_nascimento', 'idade')

from rest_framework import serializers

class PessoaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    data_nascimento = serializers.DateField()
    idade = serializers.CharField(max_length=255)

    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.nome = attrs.get('nome', instance.nome)
            instance.data_nascimento = attrs.get('data_nascimento', instance.data_nascimento)
            instance.idade = attrs.get('idade', instance.idade)
            return instance
        return Pessoa(**attrs)




# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pessoas', UserViewSet)

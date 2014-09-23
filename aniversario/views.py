from braces.views import JSONResponseMixin
from .models import Pessoa, Carro
from django.shortcuts import render
from django.db import models
from django import forms
# Create your views here.
from django.views import generic
from rest_framework import routers, serializers, viewsets


class PessoaListView(JSONResponseMixin, generic.ListView):
    model = Pessoa



class F(forms.ModelForm):

    class Meta:
        model = Carro

class Home(generic.CreateView):
    model = Carro
    template_name = 'index.html'
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

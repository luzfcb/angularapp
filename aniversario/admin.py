from django.contrib import admin

# Register your models here.
from .models import Pessoa, Carro


class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'data_nascimento', 'idade'
    ]

admin.site.register(Pessoa, PessoaAdmin)


admin.site.register(Carro)

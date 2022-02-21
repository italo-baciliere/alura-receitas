from django.shortcuts import render
from .models import Receita

def index(request):

    # dicionário
    receitas = Receita.objects.all()

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request,'index.html',dados)

def receita(request, requesta_id):
    return render(request, 'receita.html')


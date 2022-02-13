from django.shortcuts import render

def index(request):

    # dicionário
    receitas = {
        1:'Lasanha',
        2:'Sopa de legumes',
        3:'Sorvete',
        4:'Barra de cereal'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request,'index.html',dados)

def receita(request):
    return render(request, 'receita.html')


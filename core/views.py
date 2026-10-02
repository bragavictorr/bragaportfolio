
from django.shortcuts import render
from .models import Projeto

def home(request):
    # Pega todos os projetos cadastrados no banco de dados
    projetos = Projeto.objects.all()
    
    # Envia os projetos para o arquivo home.html
    return render(request, 'home.html', {'projetos': projetos})
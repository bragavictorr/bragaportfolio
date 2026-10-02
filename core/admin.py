from django.contrib import admin
from .models import Projeto

# Opção recomendada: Personalizando o painel
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    # Quais colunas vão aparecer na lista de projetos
    list_display = ('titulo', 'tecnologias', 'link_github')
    
    # Adiciona uma barra de pesquisa
    search_fields = ('titulo', 'tecnologias')

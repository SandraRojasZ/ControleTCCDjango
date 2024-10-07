from django.shortcuts import render
from .models import NovoTcc # importar a classe que foi criado no models.py

# Função HOME da pasta de TCC
def home(request):
    return render(request, 'tccs/home.html')

# FUNÇÃO ADDTCC DE CAPTURAR OS DADOS DO HOME TCC E REDIRECIONAR

# Deverá já ter uma uls/rota de tccs antes de criar uma view
# urls.py -> path('tccs/', views.addtcc, name='listagem_tccs')
# Deverá constar no models para puxar os dados dos campos da BD
# puxar a class NovoTcc que foi criado no models.py
# Django irá substituir essa linha pelo valor da lista de objetos NovoTcc.
def addtcc(request):
    # Salvar os dados da tela home.html para o bando de dados db.sqlite
    novo_tcc = NovoTcc()
    novo_tcc.nome= request.POST.get('nome') #name = "nome" no home.html
    novo_tcc.titulo= request.POST.get('titulo')
    novo_tcc.descricao = request.POST.get('descricao')
    novo_tcc.aluno1 = request.POST.get('aluno1')
    novo_tcc.aluno2 = request.POST.get('aluno2')
    novo_tcc.aluno3 = request.POST.get('aluno3')
    novo_tcc.curso = request.POST.get('curso') #name = "curso" no home.html
    novo_tcc.datafim = request.POST.get('fim')
    novo_tcc.status = request.POST.get('status')
    novo_tcc.save()
    # Exibir todos os usuários já cadastrados em uma nova página
    # Colocando em um dicionário
    dic_tcc = {
        'tccs': NovoTcc.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'tccs/tccs.html', dic_tcc)
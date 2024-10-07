"""
URL configuration for project_cont_tcc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin  # No momento não vamos usar
from django.urls import path
from app_cont_tcc import views # importando as funções

urlpatterns = [
    #path('admin/', admin.site.urls),
    # rota, view responsável, nome de referência

    # cadastro novo tcc -> página ->  tccs.com
    path('', views.home, name='home'),

    # tccs.com/lista das tccs
    # 1.criar a path da action do form do home.html (colocar na parte name a url)
    # 2.Criar na view para chamar a função desejada
    # 3.criar o banco de dados no models
    
    path('tccs/', views.addtcc, name='listagem_tcc')
]

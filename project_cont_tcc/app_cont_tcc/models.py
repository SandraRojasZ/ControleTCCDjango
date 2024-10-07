from django.db import models

# objetos pythons que representam uma tabela no Banco de Dados via Django

# urls de novo TCC
# views addtcc
class NovoTcc(models.Model):
    id_novotcc = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    aluno1 = models.CharField(max_length=255)
    aluno2 = models.CharField(max_length=255)
    aluno3 = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    datafim = models.DateField()
    status = models.CharField(max_length=255)

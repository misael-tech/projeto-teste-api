from django.db import models

# Create your models here.
class Tarefa(models.Model):

    
    titulo = models.CharField(max_length=100)
    #blank=true : texto nao obrigatorio
    descricao = models.TextField(blank=True)
    # sera preenchido automaticamente na criação.
    criada_em = models.DateTimeField(auto_now_add=True)


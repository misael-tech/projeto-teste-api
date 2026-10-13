from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tarefa 
from .serializers import TarefaSerializer

@api_view(["GET"])
def mostrar_tarefas(request):
    listar_tarefas = Tarefa.objects.all()
    dados = TarefaSerializer(listar_tarefas,many=True)
    
    return Response(dados.data,status=200)

@api_view(["GET""POST"])

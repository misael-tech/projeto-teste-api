from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tarefa 
from .serializers import TarefaSerializer
from rest_framework import status



@api_view(["GET"])
def mostrar_tarefas(request):
    listar_tarefas = Tarefa.objects.all()
    dados = TarefaSerializer(listar_tarefas,many=True)
    
    return Response(dados.data,status=200)

@api_view(["GET" ,"POST"])
def enviar_tarefa(request):

    enviar_tarefas = TarefaSerializer(data=request.data)

    if enviar_tarefas.is_valid():
        enviar_tarefas.save()
        return Response(
            enviar_tarefas.data,
            status=status.HTTP_201_CREATED
            
        )

    return Response(
        enviar_tarefas.errors,
        status=status.HTTP_400_BAD_REQUEST
    )



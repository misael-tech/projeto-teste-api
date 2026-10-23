from django.contrib import admin
from django.urls import path
from .views import mostrar_tarefas,enviar_tarefa

urlpatterns = [
    path("api/tarefas/",view=mostrar_tarefas,name="mostrar_tarefas"),
    path('api/criar/tarefas/', enviar_tarefa, name='criar_tarefa'),
]




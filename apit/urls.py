from django.contrib import admin
from django.urls import path
from .views import mostrar_tarefas

urlpatterns = [
    path("api/tarefas/",view=mostrar_tarefas,name="mostrar_tarefas")
]




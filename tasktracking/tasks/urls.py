from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_tarefa', views.cadastrar_tarefa, name='cadastrar_tarefa'),
]
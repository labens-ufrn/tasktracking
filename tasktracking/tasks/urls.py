from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_tarefa', views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path('detalhar_tarefa/<int:pk>/', views.TarefaDetailView.as_view(), name='detalhar_tarefa'),
    path('cadastrar_link', views.cadastrar_link, name='cadastrar_link'),
    path('cadastrar_tag', views.cadastrar_tag, name='cadastrar_tag'),
    path('pesquisar_tarefas', views.buscar_tarefas, name='buscar_tarefas'),
    path('cadastrar_execucao', views.cadastrar_execucao, name='cadastrar_execucao'),
]

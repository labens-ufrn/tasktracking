from django.http import request
from django.shortcuts import redirect, render
from tasks.forms import TarefaForm

from tasks.models import Tarefa
from tasks.models import Link

def index(request):
    """View function for home page of site."""

    lista_tarefas = Tarefa.objects.all()
    lista_link = Link.objects.all()

    context = {
        'lista_tarefas': lista_tarefas
    }

    return render(request, 'tasks/index.html', context=context)


def cadastrar_tarefa(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            form_tarefa.save()
            return redirect('index')
    else:
        form_tarefa = TarefaForm()

    context = {
        'form_tarefa': form_tarefa
    }
    return render(request, 'tasks/tarefa/cadastrar_tarefa.html', context=context)

def cadastrar_link(request):
    if request.method == 'POST':
        form_link = LinkForm(request.POST)
        if form_link.is_valid():
            form_link.save()
            return redirect('index')
    else:
        form_link = LinkForm()

    context = {
        'form_link': form_link
    }
    return render(request, 'tasks/link/cadastrar_link.html', context=context)


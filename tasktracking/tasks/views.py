from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from tasks.forms import LinkForm, TarefaForm, TagForm

from tasks.models import Tarefa
from tasks.models import Link
from tasks.models import Tag

def index(request):
    """View function for home page of site."""

    lista_tarefas = Tarefa.objects.all()
    lista_link = Link.objects.all()
    lista_tag = Tag.objects.all()

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


class TarefaDetailView(DetailView):
    model = Tarefa
    template_name = 'tasks/tarefa/detalhar.html'


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


def cadastrar_tag(request):
    if request.method == 'POST':
        form_tag = TagForm(request.POST)
        if form_tag.is_valid():
            form_tag.save()
            return redirect('index')
    else:
        form_tag = TagForm()

    context = {
        'form_tag': form_tag
    }
    return render(request, 'tasks/tags/cadastrar_tag.html', context=context)


def buscar_tarefas(request):

    search = request.POST.get("search")

    lista_tarefas = Tarefa.objects.filter(nome__icontains=search)

    context = {
       'lista_tarefas': lista_tarefas
    }
    return render(request, 'tasks/index.html', context=context)
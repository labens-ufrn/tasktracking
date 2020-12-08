from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from datetime import datetime
from tasks.forms import LinkForm, TarefaForm, TagForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Execucao, Tarefa
from tasks.models import Link
from tasks.models import Tag

def index(request):
    """View function for home page of site."""

    lista_tarefas  = Tarefa.objects.all().order_by('-criada_em')

    paginator = Paginator(lista_tarefas, 3)

    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1

    lista_tarefas_paginada = paginator.get_page(page_number)

    context = {
        'lista_tarefas_paginada': lista_tarefas_paginada
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


def cadastrar_execucao(request):
    tarefa_pk = request.GET.get('tarefa_pk')
    print('Passando na View!' + tarefa_pk)

    tarefa = Tarefa.objects.get(pk=tarefa_pk)
    inicio = datetime.now()
    Execucao.objects.create(
        inicio=inicio, tarefa=tarefa, 
        status=Execucao.EXECUTANDO,
        usuario=tarefa.usuario)
    
    data = dict()
    return JsonResponse(data)


def stop_execucao(request):
    # Buscar uma execução da tarefa selecionda que esteja EXECUTANDO
    # Colocar o status PARADA e a data de fim.
    data = dict()
    return JsonResponse(data)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

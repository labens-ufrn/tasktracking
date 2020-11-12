from django import forms
from tasks.models import Link, Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'

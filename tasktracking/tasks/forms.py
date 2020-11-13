from django import forms
from tasks.models import Link, Tarefa, Tag


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
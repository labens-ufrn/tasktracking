from django.contrib import admin

from tasks.models import Execucao, Link, Tag, Tarefa, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tag)
admin.site.register(Link)
admin.site.register(Tarefa)
admin.site.register(Execucao)


from django.contrib import admin
from .models import Status, Categoria, Chamado, Atendimento, Funcionario


admin.site.register(Status)
admin.site.register(Categoria)
admin.site.register(Chamado)
admin.site.register(Atendimento)
admin.site.register(Funcionario)

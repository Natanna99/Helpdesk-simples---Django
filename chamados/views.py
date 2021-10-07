from django.shortcuts import render

from django.urls import reverse
from .models import Chamado,Funcionario,Status, Atendimento
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import ChamadoForm, AtendimentoForm

def inicial(request):
    if request.user.is_authenticated:
        return render(request, 'chamados/inicial.html', {'chamados': chamados})
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})
def chamados(request):
    chamados = []
    if request.user.is_authenticated:
        if request.user.is_superuser:
            chamados = Chamado.objects.filter()
        else:
            chamados = Chamado.objects.filter(autor__usuario=request.user)
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})

    return render(request, 'chamados/chamados.html', {'chamados': chamados})


def detalhes(request, id_chamado):
    if request.user.is_authenticated:
        chamado = Chamado.objects.get(pk=id_chamado)
        return render(request, 'chamados/detalhes.html', {'chamado': chamado})
    else:
        return render(request, 'chamados/erro_autenticacao.html', {})

class ChamadoView(FormView):
    template_name = "chamados/add_chamado.html"
    form_class = ChamadoForm
    def form_valid(self, form):
        dados = form.clean()
        mensagem = Chamado(titulo=dados['titulo'], descricao=dados['descricao'],
                           telefone=dados['telefone'], categoria=dados['categoria'],
                           autor=Funcionario.objects.get(usuario=self.request.user), 
                           status=Status.objects.get(nome='Aberto'))
        mensagem.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('chamado_sucesso')


class ChamadoSucessoView(TemplateView):
    template_name = "chamados/chamado_sucesso.html"

class AtendimentoView(FormView):
    template_name = "chamados/add_atendimento.html"
    form_class = AtendimentoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = Atendimento(descricao=dados['descricao'], chamado=dados['chamado'],
                           atendente=Funcionario.objects.get(usuario=self.request.user))
        dados['chamado'].status=dados['status']
        dados['chamado'].save()
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('atendimento_sucesso')


class AtendimentoSucessoView(TemplateView):
    template_name = "chamados/atendimento_sucesso.html"
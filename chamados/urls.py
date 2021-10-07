from django.contrib import admin
from django.urls import path, include

from .views import inicial,chamados, detalhes, ChamadoView, ChamadoSucessoView, AtendimentoView, AtendimentoSucessoView

urlpatterns = [
    path('', inicial, name='inicial'),
    path('chamados/', chamados, name='chamados'),
    path('detalhes/<int:id_chamado>', detalhes, name='detalhes'),
    path('addchamado/', ChamadoView.as_view(), name='add_chamado'),
    path('chamadosucesso/', ChamadoSucessoView.as_view(), name='chamado_sucesso'),
    path('addatendimento/', AtendimentoView.as_view(), name='add_atendimento'),
    path('atendimentosucesso/', AtendimentoSucessoView.as_view(), name='atendimento_sucesso'),
]
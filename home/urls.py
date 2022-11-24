from cgitb import lookup
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import path, include
from . import views

routers = routers.DefaultRouter()
routers.register('cliente', views.ClienteViewSet)
routers.register('novocliente', views.ClienteInViewSet)

routers.register('usuario', views.UsuarioViewSet)
routers.register('endereco', views.EnderecoViewSet)
routers.register('contatos', views.ContatosViewSet)
routers.register('favoritos', views.FavoritosViewSet)
routers.register('conta', views.ContaViewSet)
routers.register('emprestimos', views.EmprestimosViewSet)
routers.register('pagamentoemprestimo', views.PagamentoEmprestimoViewSet)
routers.register('extrato', views.ExtratoViewSet)
routers.register('cartao', views.CartaoViewSet)
routers.register('transacoes', views.TransacoesViewSet)
routers.register('fatura', views.FaturaViewSet)
routers.register('solicitacao', views.SolicitacaoViewSet)

urlpatterns = routers.urls
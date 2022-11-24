from django.contrib import admin

from home.models import *


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'sexo', 'data_nacimento')
    list_display_links = ('nome_completo', )
    list_per_page = 10

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cpf', 'estado')
    list_display_links = ('cliente', )
    list_per_page = 10

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cep', 'uf')
    list_display_links = ('cliente', )
    list_per_page = 10

class FavoritosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'destinatario')
    list_display_links = ('nome', )
    list_per_page = 10

class ContatosAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'telefone', 'email')
    list_display_links = ('cliente', )
    list_per_page = 10

class ContaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'agencia')
    list_display_links = ('id', )
    list_per_page = 10

class EmprestimosAdmin(admin.ModelAdmin):
    list_display = ('conta', 'juros', 'validade')
    list_display_links = ('conta', )
    list_per_page = 10

class PagamentoEmprestimoAdmin(admin.ModelAdmin):
    list_display = ('emprestimo', 'parcelas', 'data_vencimento')
    list_display_links = ('emprestimo', )
    list_per_page = 10

class ExtratoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'valor', 'data')
    list_display_links = ('conta', )
    list_per_page = 10

class CartaoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'tipo')
    list_display_links = ('conta', )
    list_per_page = 10

class TransacoesAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data')
    list_display_links = ('valor', )
    list_per_page = 10

class FaturaAdmin(admin.ModelAdmin):
    list_display = ('cartao', 'valor', 'data_validade')
    list_display_links = ('cartao', )
    list_per_page = 10

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'data_solicitacao', 'aprovacao')
    list_display_links = ('conta', )
    list_per_page = 10


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Favoritos, FavoritosAdmin)
admin.site.register(Contatos, ContatosAdmin)
admin.site.register(Conta, ContaAdmin)
admin.site.register(Emprestimos, EmprestimosAdmin)
admin.site.register(PagamentoEmprestimo, PagamentoEmprestimoAdmin)
admin.site.register(Extrato, ExtratoAdmin)
admin.site.register(Cartao, CartaoAdmin)
admin.site.register(Transacoes, TransacoesAdmin)
admin.site.register(Solicitacao, SolicitacaoAdmin)
admin.site.register(Fatura, FaturaAdmin)
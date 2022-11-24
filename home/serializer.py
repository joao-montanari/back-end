from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome_completo', 'data_nacimento', 'empregado', 'sexo', 'foto']
    foto = PictureField()

class ClienteInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome_completo', 'data_nacimento', 'empregado', 'sexo', 'foto']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'cpf', 'senha', 'estado', 'cliente']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'pais', 'uf', 'cidade', 'bairro', 'rua', 'logradouro', 'numero', 'cep', 'cliente']

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatos
        fields = ['id', 'telefone', 'email', 'cliente']

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ['id', 'nome', 'remetente', 'destinatario']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'saldo', 'salario', 'numero', 'agencia', 'tipo', 'cliente']

class EmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = ['id', 'valor', 'valor_com_juros', 'data', 'juros', 'validade', 'condicao', 'conta']

class PagamentoEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagamentoEmprestimo
        fields = ['id', 'parcelas', 'data_vencimento', 'data_pagamento', 'emprestimo']

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['id', 'valor', 'data', 'descricao', 'tipo', 'conta']

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id', 'numero', 'cvv', 'data_validade', 'tipo', 'estado', 'conta']

class TransacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = ['id', 'valor', 'data', 'destinatario', 'remetente']

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = ['id', 'valor', 'data_validade', 'data_pagamento', 'cartao']

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = ['id', 'data_resposta', 'data_solicitacao', 'aprovacao', 'conta']
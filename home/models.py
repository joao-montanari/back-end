from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.db import models
from pictures.models import PictureField

# Create your models here.

class Cliente(models.Model):
    MASCULINO = 'M'
    FEMININO = 'F'
    INDEFINIDO = 'I'

    GENERO = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
        (INDEFINIDO, 'Indefinido')
    ]

    nome_completo = models.CharField(max_length=100)
    data_nacimento = models.DateField()
    empregado = models.BooleanField()
    sexo = models.CharField(
        max_length = 1,
        choices = GENERO,
        default = INDEFINIDO,
    )
    # foto = models.ImageField(upload_to = 'clientes/imagens')
    foto = PictureField(upload_to = 'clientes/imagens')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.nome_completo

class Usuario(models.Model):
    cpf = models.CharField(max_length=14)
    senha = models.CharField(max_length=16)
    estado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Endereco(models.Model):
    pais = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=30)
    numero = models.PositiveSmallIntegerField()
    cep = models.CharField(max_length=9)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Contatos(models.Model):
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Favoritos(models.Model):
    nome = models.CharField(max_length=100)
    remetente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='remetente')
    destinatario = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='destinatario')

class Conta(models.Model):
    CORRENTE = 'C'
    POUPANCA = 'P'
    SALARIO = 'S'

    TIPO_CONTA = [
        (CORRENTE, 'Corrente'),
        (POUPANCA, 'Poupanca'),
        (SALARIO, 'Salario'),
    ]

    saldo = models.DecimalField(max_digits=10,decimal_places=2)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    numero = models.PositiveIntegerField()
    agencia = models.PositiveIntegerField()
    tipo = models.CharField(
        max_length=1,
        choices=TIPO_CONTA,
        default=CORRENTE,
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Emprestimos(models.Model):
    APROVADO = 'A'
    REPROVADO = 'R'
    PAGANDO = 'P'
    FINALIZADO = 'F'
    ESPERA = 'E'

    CONDICAO = [
        (APROVADO, 'Aprovado'),
        (REPROVADO, 'Reprovado'),
        (PAGANDO, 'Pagando'),
        (ESPERA, 'Em espera para aprovação'),
        (FINALIZADO, 'Finalizado'),
    ]

    valor = models.DecimalField(max_digits=10,decimal_places=2)
    valor_com_juros = models.DecimalField(max_digits=10,decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    juros = models.DecimalField(max_digits=10,decimal_places=2)
    validade = models.DateField()
    condicao = models.CharField(
        max_length=1,
        choices=CONDICAO,
        default=ESPERA,
    )
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)

class PagamentoEmprestimo(models.Model):
    parcelas = models.PositiveSmallIntegerField()
    data_vencimento = models.DateTimeField(auto_now_add=True)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    emprestimo = models.ForeignKey(Emprestimos, on_delete=models.PROTECT)

class Extrato(models.Model):
    ENTRADA = 'E'
    SAIDA = 'S'

    TIPOS = [
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saida'),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS,
        default=SAIDA
    )
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)



class Cartao(models.Model):
    DEBITO = 'D'
    CREDITO = 'C'

    TIPOS = [
        (DEBITO, 'Debito'),
        (CREDITO, 'Credito'),
    ]

    numero = models.CharField(max_length=20)
    cvv = models.PositiveSmallIntegerField()
    data_validade = models.DateField()
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS,
        default=DEBITO,
    )
    estado = models.BooleanField()
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)

class Transacoes(models.Model):
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    destinatario = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='destinatario')
    remetente = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='remetente')

class Fatura(models.Model):
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    data_validade = models.DateField()
    data_pagamento = models.DateTimeField(auto_now_add=True)
    cartao = models.ForeignKey(Cartao, on_delete=models.PROTECT)

class Solicitacao(models.Model):
    data_resposta = models.DateTimeField(auto_now_add=True)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    aprovacao = models.BooleanField()
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)

# class Cliente(models.Model):
#     nome = models.CharField(max_length = 255)
#     celular = models.CharField(max_length = 50)
#     dt_nascimento = models.DataField()


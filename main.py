from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        conta = cls(numero, cliente)
        cliente.adicionar_conta(conta)
        return conta

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500.0, limite_saques=3, agencia="0001"):
        super().__init__(numero, cliente, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques excedido!")
            return False
        if valor > 0 and (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self.numero_saques += 1
            return True
        return False

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

# Criando cliente
cliente1 = PessoaFisica(nome="Ana", cpf="12345678900", data_nascimento="01/01/1990", endereco="Rua A, 100")

# Criando conta
conta1 = ContaCorrente.nova_conta(cliente1, numero=1)

# Fazendo um depósito
deposito = Deposito(500)
cliente1.realizar_transacao(conta1, deposito)

# Fazendo um saque
saque = Saque(200)
cliente1.realizar_transacao(conta1, saque)

print("Saldo:", conta1.saldo_atual())
print("Histórico de transações:", conta1.historico.transacoes)

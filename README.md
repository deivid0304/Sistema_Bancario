# 💰 Sistema Bancário Orientado a Objetos (Python)

Um sistema bancário simples e didático desenvolvido em Python, utilizando **paradigma orientado a objetos** (POO), seguindo modelo inspirado em UML.

Este projeto foi criado com o objetivo de praticar os principais pilares da POO: **Herança, Abstração, Encapsulamento e Polimorfismo**, além de preparar a estrutura para futuras melhorias como persistência de dados e interface gráfica.

---

## 📘 Diagrama de Classes (Baseado no UML)

Cliente
├─ PessoaFisica
├─ Conta
│ ├─ ContaCorrente
├─ Historico
└─ Transacao (classe abstrata)
├─ Saque
└─ Deposito

yaml
Copiar
Editar

---

## ✅ Funcionalidades Implementadas

- Cadastro de cliente (Pessoa Física)
- Criação de conta vinculada ao cliente
- Depósitos e saques através de objetos da classe `Transacao`
- Controle de limite e quantidade de saques na conta corrente
- Registro de histórico de transações com data e hora
- Método `nova_conta()` como *factory method*

---

## 🧠 Conceitos Aplicados

- Abstração com classe abstrata `Transacao`
- Herança entre `Cliente` → `PessoaFisica`
- Polimorfismo nos tipos de transação
- Encapsulamento do saldo e histórico dentro da classe `Conta`
- Padrão de projeto Factory (método `nova_conta`)

---

## 🧪 Exemplo de Uso Rápido

```python
from classes import PessoaFisica, ContaCorrente, Deposito, Saque

cliente1 = PessoaFisica(
    nome="Ana Souza",
    cpf="12345678900",
    data_nascimento="1990-01-01",
    endereco="Rua A"
)

conta1 = ContaCorrente.nova_conta(cliente1, numero=1)

# Depósito
deposito = Deposito(500)
cliente1.realizar_transacao(conta1, deposito)

# Saque
saque = Saque(200)
cliente1.realizar_transacao(conta1, saque)

print("Saldo atual:", conta1.saldo_atual())
print("Histórico:", conta1.historico.transacoes)
🛠 Próximas Evoluções
Salvamento em arquivo JSON

Interface em terminal com menu interativo

Versão com Tkinter ou Flask

Exportar o histórico em .txt ou .pdf

🚀 Tecnologias Utilizadas
Python 3.11+

Paradigma Orientado a Objetos

Módulo abc (classes abstratas)

Módulo datetime

📂 Estrutura Recomendada
css
Copiar
Editar
project/
├─ classes.py
├─ main.py
└─ README.md
⚠️ Aviso
Este projeto tem fins educacionais e não deve ser usado como sistema bancário real sem camadas de segurança, banco de dados, controle de exceções e autenticação adequada.

# Autor
Desenvolvido por Deivid Ferreira — projeto de estudo para transição de carreira e aprofundamento em Python / POO.

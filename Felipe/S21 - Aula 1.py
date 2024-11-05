class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []

    def consultar_saldo(self):
        print("Saldo: R$",self.saldo)

    def consultar_transacoes(self):
        print("Transações:", self.transacoes)

    def depositar(self, valor): 
        self.saldo += valor 
        print("Você depositou: R$",valor)
        self.registrar_transacao("Depósito", valor)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)
            print("Você sacou: R$", valor)
        else:
            print("Saldo insuficiente.")

    def registrar_transacao(self, tipo, valor):
        self.transacoes.append({"Tipo": tipo, "Valor": valor})


# cb = ContaBancaria("5542779")
# cb.consultar_saldo()
# cb.depositar(50)
# cb.consultar_saldo()
# cb.consultar_transacoes()
# cb.sacar(45)
# cb.consultar_saldo()

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, limite_cheque_especial=0):
        super().__init__(numero_conta)
        self.limite_cheque_especial = limite_cheque_especial
    def emitir_cheque(self, valor):
        if self.saldo + self.limite_cheque_especial >= valor:
            self.saldo -= valor
            self.registrar_transacao("Emissão de Cheque", valor)
        else:
            print("Limite de cheque especial excedido.")

# cc = ContaCorrente("88990011",1000)
# cc.depositar(500)
# cc.emitir_cheque(1000)
# cc.consultar_saldo()
# cc.emitir_cheque(400)
# cc.consultar_saldo()
# cc.emitir_cheque(400)

class ContaPoupanca(ContaBancaria):
    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * (taxa_juros / 100)
        self.saldo += juros
        self.registrar_transacao("Juros Mensais", juros)

# cp = ContaPoupanca("9293847983", 9000)
# cp.calcular_juros_mensal(0.4)

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero_conta):
       super().__init__(numero_conta, saldo=0)
       self.investimentos = []
       self.valorMaximo = 0
    def registrar_investimentos(self, tipo, produto, valor):
        if self.saldo >= valor:
            self.investimentos.append({"Tipo":tipo, "Produto": produto, "Valor": valor})
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    def somartudo(self):
        for x in self.investimentos:
            self.valorMaximo += x["Valor"]

ci = ContaInvestimento("2234124213")
ci.saldo = 7000000
ci.registrar_investimentos("Tesouro Direto", "Selic", 67)
ci.registrar_investimentos("Tesouro Direto", "Selic", 30)
ci.registrar_investimentos("Tesouro Direto", "Selic", 70)
ci.registrar_investimentos("Tesouro Direto", "Selic", 43)
ci.registrar_investimentos("Tesouro Direto", "Selic", 25)
ci.registrar_investimentos("Tesouro Direto", "Selic", 55)
ci.registrar_investimentos("Tesouro Direto", "Selic", 36)
ci.registrar_investimentos("Tesouro Direto", "Selic", 28)
ci.registrar_investimentos("Tesouro Direto", "Selic", 72)
ci.registrar_investimentos("Tesouro Direto", "Selic", 90)
ci.registrar_investimentos("Tesouro Direto", "Selic", 200)
ci.registrar_investimentos("Tesouro Direto", "Selic", 250)
ci.registrar_investimentos("Tesouro Direto", "Selic", 5)
ci.registrar_investimentos("Tesouro Direto", "Selic", 50)
ci.registrar_investimentos("Tesouro Direto", "Selic", 25)
ci.somartudo()
print(ci.valorMaximo)
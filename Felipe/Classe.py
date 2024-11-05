class Funcionario:
    def __init__(self, id, nome, cargo, salario):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def Bonus(self):
        resultado = self.salario * 1.10
        return resultado
    
class Gerente(Funcionario):
    def __init__(self, id, nome, cargo, salario, regiao ):
        super().__init__(id, nome, cargo, salario)
        self.regiao = regiao
    
    def Bonus(self):
        resultado = super().Bonus() * 1.20
        return resultado

class Vendedor(Gerente):
    def __init__(self, id, nome, cargo, salario, regiao, comissao):
        super().__init__(id, nome, cargo, salario, regiao)
        self.comissao = comissao
    
    def Bonus(self):
        return self.salario * 1.15
    
g1 = Gerente("1", "Douglas", "Gerente Administrativo", 10000, "Sudeste")
print(g1.Bonus())

v1 = Vendedor("28", "Mario", "Vendedor de Eletrônico", 1800, "Sudeste", 5)
print(v1.Bonus())
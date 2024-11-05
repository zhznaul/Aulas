class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def Aumento(self): 
        resultado = self.salario * 2
        return resultado
    def ganhoAnual(self):
        ganhoanual = self.salario * 12
        return ganhoanual
    def exibeDados(self):
        return (f"Aumento: {self.Aumento()}, Ganho Anual: {self.ganhoAnual()}")

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula
    def getMatricula(self):
        return self.matricula
    def setMatricula(self, nova_matricula):
        self.matricula = nova_matricula
    def exibeDados(self):
        super().exibeDados()
        print("Matrícula:",self.matricula)

class Tecnico(Assistente):
    def BonusTecnico(self):
        self.salario = self.salario * 1.1
        return self.salario
    def ganhoAnual(self):
        ganhoanual = self.BonusTecnico() * 12
        return ganhoanual

class Administrativo(Assistente):
    def BonusAdministrativo(self):
        resultado = self.salario * 1.05
        return resultado
    def ganhoAnual(self):
        ganhoanual = self.BonusAdministrativo() * 12
        return ganhoanual
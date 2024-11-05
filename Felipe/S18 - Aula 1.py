class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.curtidas = 0
    def imprimir(self):
        print (f"Nome : {self.nome}, Telefone: {self.telefone}, Empresa {self.empresa}, Curtidas: {self.curtidas}")
perfilVip = Perfil("Domau", "Não informado", "Nike")
perfilVip.imprimir()
perfilVip.curtidas =+ 1
perfilVip.curtidas =+ 1
perfilVip.curtidas =+ 1
perfilVip.curtidas =+ 1
perfilVip.curtidas =+ 1
perfilVip.imprimir()
perfilVip.curtidas = 1000
perfilVip.imprimir()

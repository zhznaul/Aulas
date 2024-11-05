class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.__nome = nome
        self.__telefone = telefone
        self.__empresa = empresa
        self.__curtidas = 0
    def imprimir(self):
        print (f"Nome : {self.__nome}, Telefone: {self.__telefone}, Empresa {self.__empresa}, Curtidas: {self.__curtidas}")
    def somarCurtidas(self):
        self.__curtidas=+1
    def mostrarCurtidas(self):
        print(f"Numero de curtidas: {self.__curtidas}")
perfilVip = Perfil("Domau", "Não informado", "Nike")
perfilVip.__curtidas = 1000
perfilVip.imprimir()
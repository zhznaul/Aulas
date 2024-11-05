#Public - O acesso é livre em qualquer parte do programa. Qualquer objeto ou classe no mesmo projeto pode acessar o modificador public.
#Private - O acesso é permitido somente dentro da classe onde um modificador foi declarado. O modificador private restringe completamente o acesso a um recurso de classe de todas as outras classes.
#Protected - O modificador protected torna um membro acessivel da classe do mesmo pacote ou atraves da herança. Os membros herdados não são acessiveis a outras classes fora do pacote em que foram declarados.

class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
    def imprimir(self):
        print("Estou dentro da função imprimir")
        print(f"Nome: {self.nome} idade: {self.idade} peso: {self.peso}")
p1= Pessoa ("Hugo", 55, 105)
p2 = Pessoa("Renan", 25, 75)
p3 = Pessoa ("Jeniffer", 45, 70)
print(p1.nome)
p3.imprimir()
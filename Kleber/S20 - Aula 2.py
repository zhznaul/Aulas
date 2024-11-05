def soma():
    print("\nEscolha dois números para soma-los.")
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    print("O resultado dessa operação é:", x+y)
def subtracao():
    print("\nEscolha dois números para subtrair.")
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    print("O resultado dessa operação é:", x-y)
def multiplicacao():
    print("\nEscolha dois números para multiplicar-los.")
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    print("O resultado dessa operação é:", x*y)
def divisao():
    print("\nEscolha dois números para dividir-los.")
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    print("O resultado dessa operação é:", x/y)
def menu():
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        soma()
        pass
    elif escolha == "2":
        subtracao()
        pass
    elif escolha == "3":
        multiplicacao()
        pass
    elif escolha == "4":
        divisao()
        pass
    elif escolha == "5":
        print("Saindo.")
        break
    else:
        print("Opção invalida. Tente novamente.")
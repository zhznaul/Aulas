import random
def aleatorio(valor):
    return random.randint(0,valor)
numero_aleatorio = aleatorio(100)
while True:
    quest = int(input("\nDigite um número: "))
    if quest > numero_aleatorio:
        print("O número que você digitou é maior.")
    elif quest < numero_aleatorio:
        print("O número que você digitou é menor.")
    else:
        print(f"Parabéns você acertou o número. ({numero_aleatorio})")
        break
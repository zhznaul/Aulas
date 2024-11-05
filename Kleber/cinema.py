def reservar(sala, fileira, cadeira):
    if sala[fileira-1][cadeira-1] == 0:
        sala[fileira-1][cadeira-1] = 1
        print(f"Você reservou a cadeira número {cadeira} da fileira {fileira}.")
    else:
        print("Este lugar já está reservado.")

def cancelar_reserva(sala, fileira, cadeira):
    if sala[fileira-1][cadeira-1] == 1:
        sala[fileira-1][cadeira-1] = 0
        print("Você cancelou a reserva dessa cadeira.")
    else:
        print("Este lugar não está reservado.")

def exibir_sala(sala):
    for fila in sala:
        print(" ".join(map(str,fila)))

def menu():
    print("O que deseja fazer?")
    print("1. Reservar uma cadeira")
    print("2. Cancelar reserva de uma cadeira")
    print("3. Mapa das cadeiras")
    print("4. Sair")

sala = [[0]*8 for fila in range(5)]

while True:
    menu()
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        fileira = int(input("Qual fileira você deseja reservar? "))
        cadeira = int(input("Qual cadeira você deseja reservar? "))
        reservar(sala, fileira, cadeira)
        exibir_sala(sala)
    elif escolha == 2:
        fileira = int(input("Qual fileira você deseja cancelar a reservar? "))
        cadeira = int(input("Qual cadeira você deseja cancelar a reservar? "))
        cancelar_reserva(sala, fileira, cadeira)
        exibir_sala(sala)
    elif escolha == 3:
        exibir_sala(sala)
    elif escolha == 4:
        print("Você saiu com sucesso.")
        break
    else:
        print("O número que foi inserido é invalido.")
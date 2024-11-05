artistas=[]

def novo_artista(artista):
    artistas.append(artista)
    print(artistas)

def sub_artista(antigo, novo):
    indice = artistas.index(antigo)
    artistas[indice] = novo
    print(artistas)

def lista_atual():
    print(artistas)

def menu():
    print("----------SISTEMA DE AGENDAMENTO DE SHOWS----------")
    print("\nMenu:")
    print("1. Substituir artista")
    print("2. Adicionar artista")
    print("3. Lista atualizada")
    print("4. Sair")

while True:
    menu()
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        antigo = input("Insira o nome do artista que será substituido: ")
        novo = input("Insira o nome do novo artista: ")
        sub_artista(antigo,novo)
    elif escolha == 2:
        novo = input("Insira o nome do novo artista: ")
        novo_artista(novo)
    elif escolha == 3:
        lista_atual()
    elif escolha == 4:
        break
    else:
        print("Algo deu errado.")
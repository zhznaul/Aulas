tabuleiro = [['~'] * 10 for i in range(10)]
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

def colocar_navio(tabuleiro, linha_inicial, coluna_inicial, tamanho, orientacao):
    if orientacao == 'horizontal':
        for i in range(tamanho):
            tabuleiro[linha_inicial][coluna_inicial + i] = '#'
    elif orientacao == 'vertical':
        for i in range(tamanho):
            tabuleiro[linha_inicial + i][coluna_inicial] = '#'

def tiro(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '#':
        tabuleiro[linha][coluna] = 'X'
        print("Você acertou!!!")
        return True
    
    elif tabuleiro[linha][coluna] == '~':
        tabuleiro[linha][coluna] = 'o'
        print("Você errou :(")
        return False
    
    else:
        print("VocÊ ja atirou aqui!")
        return False
    
def jogo():
    #Criar os campos dos jogadores
    tamanho = 10
    tabuleiro_jogador1 = [['~'] * tamanho for i in range(tamanho)]
    tabuleiro_jogador2 = [['~'] * tamanho for i in range(tamanho)]
    
    #Colocar os navios
    colocar_navio(tabuleiro_jogador1,1,2,3,'vertical')
    colocar_navio(tabuleiro_jogador2,3,4,2,'horizontal')

    while True:
        print("Vez do Jogador 1:")
        imprimir_tabuleiro(tabuleiro_jogador2)
        x = int(input("Jogador 1 escolhe a linha do tiro: (0 a 9)"))
        y = int(input("Jogador 1 escolhe a coluna do tiro: (0 a 9)"))
        tiro(tabuleiro_jogador2,x,y)

        if all(cell !='#' for row in tabuleiro_jogador2 for cell in row):
            print("Jogador 1 venceu!")
            break

        print("Vez do Jogador 2:")
        imprimir_tabuleiro(tabuleiro_jogador2)
        x = int(input("Jogador 2 escolhe a linha do tiro: (0 a 9)"))
        y = int(input("Jogador 2 escolhe a coluna do tiro: (0 a 9)"))
        tiro(tabuleiro_jogador1,x,y)

        if all(cell !='#' for row in tabuleiro_jogador1 for cell in row):
            print("Jogador 2 venceu!")
            break
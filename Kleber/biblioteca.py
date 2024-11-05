biblioteca = []

def add_livro(titulo, autor, genero):
    livro = {'titulo':titulo, 'autor':autor, 'genero':genero, 'disponivel':True}
    biblioteca.append(livro)
    print(f"Você adicionou o livro {titulo} com sucesso!")

def remover_livro(titulo, autor):
    for livro in biblioteca:
        if livro['titulo'] == titulo and livro['autor'] == autor:
            biblioteca.remove(livro)
            print(f"O livro {titulo} do autor {autor} foi removido da biblioteca.")
            return
        else:
            print(f"O livro {titulo} não foi encontrado.")

def contar_livro(biblioteca):
    len(biblioteca)
    contagem = len(biblioteca)
    print(f"Existem {contagem} livro(s) na biblioteca.")

#Tá errado precisa arrumar
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower == titulo:
            if livro['disponivel'] == True:
                print(f"O livro {titulo} foi encontrado e está disponível na biblioteca.")
                return
            else:
                print(f"O livro {titulo} foi escontrado porém está indisponível na biblioteca.")
                return
        else:
            print(f"O livro {titulo} não foi encontrado na biblioteca.")

def listar_livro():
    if not biblioteca:
        print("Nenhum livro na biblioteca!")
    else:
        print("Nossa biblioteca conta com os seguintes livros:")
        for livro in biblioteca:
            print(f"Titulo: {livro['titulo']} \nAutor: {livro['autor']} \nGenero: {livro['genero']}")

def disponibilidade_livro(titulo):
   for livro in biblioteca:
        if livro['titulo'] == titulo:
           if livro['disponivel'] == True:
               print("O livro está disponível na biblioteca")
               return
           else:
               print("O livro não está disponível na biblioteca.")
               return
        else:
            print("O Livro não foi encontrado.")
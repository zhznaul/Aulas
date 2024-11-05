biblioteca = []

def add_livro(titulo, autor, genero):
    livro = {'titulo': titulo, 'autor': autor, 'genero': genero, 'disponivel': True}
    biblioteca.append(livro)
    print(f"Você adicionou o livro '{titulo}' com sucesso!")

def remover_livro(titulo, autor):
    for livro in biblioteca:
        if livro['titulo'] == titulo and livro['autor'] == autor:
            biblioteca.remove(livro)
            print(f"O livro '{titulo}' do autor '{autor}' foi removido da biblioteca.")
            return
    print(f"O livro '{titulo}' do autor '{autor}' não foi encontrado.")

def contar_livros():
    contagem = len(biblioteca)
    print(f"Existem {contagem} livro(s) na biblioteca.")

def buscar_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if livro['disponivel']:
                print(f"O livro '{titulo}' foi encontrado e está disponível na biblioteca.")
            else:
                print(f"O livro '{titulo}' foi encontrado, mas está indisponível na biblioteca.")
            return
    print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

def listar_livros():
    if not biblioteca:
        print("Nenhum livro na biblioteca!")
    else:
        print("Nossa biblioteca conta com os seguintes livros:")
        for livro in biblioteca:
            print(f"Título: {livro['titulo']}\nAutor: {livro['autor']}\nGênero: {livro['genero']}\n")

def disponibilidade_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if livro['disponivel']:
                print(f"O livro '{titulo}' está disponível na biblioteca.")
            else:
                print(f"O livro '{titulo}' não está disponível na biblioteca.")
            return
    print(f"O livro '{titulo}' não foi encontrado.")

# Funções novas

def emprestar_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if livro['disponivel']:
                livro['disponivel'] = False
                print(f"O livro '{titulo}' foi emprestado com sucesso.")
            else:
                print(f"O livro '{titulo}' já está emprestado e indisponível.")
            return
    print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

def devolver_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if not livro['disponivel']:
                livro['disponivel'] = True
                print(f"O livro '{titulo}' foi devolvido e está disponível novamente.")
            else:
                print(f"O livro '{titulo}' já está disponível na biblioteca.")
            return
    print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

def listar_livros_por_genero(genero):
    encontrados = [livro for livro in biblioteca if livro['genero'].lower() == genero.lower()]
    if encontrados:
        print(f"Livros do gênero '{genero}':")
        for livro in encontrados:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}")
    else:
        print(f"Não foram encontrados livros do gênero '{genero}'.")

def atualizar_informacoes_livro(titulo, novo_titulo=None, novo_autor=None, novo_genero=None):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if novo_titulo:
                livro['titulo'] = novo_titulo
            if novo_autor:
                livro['autor'] = novo_autor
            if novo_genero:
                livro['genero'] = novo_genero
            print(f"As informações do livro '{titulo}' foram atualizadas com sucesso.")
            return
    print(f"O livro '{titulo}' não foi encontrado para atualização.")

def mostrar_menu():
    print("\nMenu Principal da Biblioteca:")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Contar Livros")
    print("4. Buscar Livro")
    print("5. Listar Todos os Livros")
    print("6. Verificar Disponibilidade do Livro")
    print("7. Emprestar Livro")
    print("8. Devolver Livro")
    print("9. Listar Livros por Gênero")
    print("10. Atualizar Informações do Livro")
    print("11. Sair")

def biblioteca_menu():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            add_livro(titulo, autor, genero)

        elif opcao == '2':
            titulo = input("Título do livro a remover: ")
            autor = input("Autor do livro a remover: ")
            remover_livro(titulo, autor)

        elif opcao == '3':
            contar_livros()

        elif opcao == '4':
            titulo = input("Título do livro a buscar: ")
            buscar_livro(titulo)

        elif opcao == '5':
            listar_livros()

        elif opcao == '6':
            titulo = input("Título do livro para verificar disponibilidade: ")
            disponibilidade_livro(titulo)

        elif opcao == '7':
            titulo = input("Título do livro para emprestar: ")
            emprestar_livro(titulo)

        elif opcao == '8':
            titulo = input("Título do livro para devolver: ")
            devolver_livro(titulo)

        elif opcao == '9':
            genero = input("Gênero dos livros a listar: ")
            listar_livros_por_genero(genero)

        elif opcao == '10':
            titulo = input("Título do livro para atualizar: ")
            novo_titulo = input("Novo título (deixe em branco para não alterar): ")
            novo_autor = input("Novo autor (deixe em branco para não alterar): ")
            novo_genero = input("Novo gênero (deixe em branco para não alterar): ")

            # Passando None caso o usuário não queira alterar o campo
            novo_titulo = novo_titulo if novo_titulo else None
            novo_autor = novo_autor if novo_autor else None
            novo_genero = novo_genero if novo_genero else None

            atualizar_informacoes_livro(titulo, novo_titulo, novo_autor, novo_genero)

        elif opcao == '11':
            print("Saindo do sistema da biblioteca. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

biblioteca_menu()

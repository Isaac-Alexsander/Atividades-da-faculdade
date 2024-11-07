def exibir_menu():
    print("1. Adicionar um livro")
    print("2. Pegar um livro Emprestado")
    print("3. Devolver um livro")
    print("4. livros disponíveis")
    print("5. Sair")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def adicionar_livro(self, biblioteca):
        titulo = input("Título do livro: ")
        autor = input("autor do livro: ")
        livro = Livro(titulo, autor)
        biblioteca.catalogo.append(livro)
        print("Livro adicionado a Biblioteca")

    def Pegar_livro(self, biblioteca):
        titulo_livro = input("Digite o livro que deseja Pegar emprestado: ")
        for livro in biblioteca.catalogo:
            if livro.titulo == titulo_livro and livro.disponivel:
                livro.disponivel = False
                self.livros_emprestados.append(livro)
                print(f"{self.nome} pegou emprestado o livro {livro}.")
                return
        print(f"O livro '{titulo_livro}' não está disponível.")

    def devolver_livro(self, biblioteca):
        titulo_livro = input("Digite o título do livro que deseja devolver: ")
        for livro in self.livros_emprestados:
            if livro.titulo == titulo_livro:
                livro.disponivel = True
                self.livros_emprestados.remove(livro)
                print(f"{self.nome} devolveu o livro {livro}.")
                return
        print(f"Não possui o livro '{titulo_livro}' para devolver.")


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def exibir_livros_disponiveis(self):
        print("\nLivros disponíveis na biblioteca:")
        disponiveis = [livro for livro in self.catalogo if livro.disponivel]
        if disponiveis:
            for livro in disponiveis:
                print(f" - {livro}")
        else:
            print("Nenhum livro disponível no momento.")

def main():
    biblioteca = Biblioteca()
    nome_usuario = input("Digite o seu nome: ")
    usuario = Usuario(nome_usuario)

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            usuario.adicionar_livro(biblioteca)
        elif opcao == '2':
            usuario.Pegar_livro(biblioteca)
        elif opcao == '3':
            usuario.devolver_livro(biblioteca)
        elif opcao == '4':
            biblioteca.exibir_livros_disponiveis()
        elif opcao == '5':
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

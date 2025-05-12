from datetime import datetime

# ===== LIVRO FÍSICO =====
class Livro:
    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"[{self.codigo}] {self.titulo} - {self.autor} ({self.ano})"

# ===== USUÁRIO =====
class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"[{self.id_usuario}] {self.nome} - {self.email}"

# ===== EMPRÉSTIMO =====
class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo=None):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo or datetime.now().strftime('%d/%m/%Y')

    def __str__(self):
        return f"{self.usuario.nome} pegou '{self.livro.titulo}' em {self.data_emprestimo}"

# ===== EBOOK =====
class Ebook:
    def __init__(self, codigo, titulo, autor, formato, preco):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.formato = formato.lower()
        self.preco = preco
        self._comprado = False

    def comprar(self):
        if self._comprado:
            print(f"Você já comprou '{self.titulo}'.")
        else:
            self._comprado = True
            print(f"Compra realizada: '{self.titulo}' por R${self.preco:.2f}.")

    def fazer_download(self):
        if self._comprado:
            print(f"Baixando '{self.titulo}' em formato {self.formato}...")
            print("Download concluído.")
        else:
            print(f"Você precisa comprar '{self.titulo}' antes de fazer o download.")

    def __str__(self):
        status = "Disponível" if not self._comprado else "Comprado"
        return f"[{self.codigo}] {self.titulo} - {self.autor} | {self.formato.upper()} | R${self.preco:.2f} | {status}"

# ===== SISTEMA BIBLIOTECA =====
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
        self.ebooks = []

    # Livros físicos
    def cadastrar_livro(self, codigo, titulo, autor, ano):
        self.livros.append(Livro(codigo, titulo, autor, ano))
        print("Livro físico cadastrado com sucesso.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro físico cadastrado.")
        else:
            for livro in self.livros:
                print(livro)

    # Usuários
    def cadastrar_usuario(self, id_usuario, nome, email):
        self.usuarios.append(Usuario(id_usuario, nome, email))
        print("Usuário cadastrado com sucesso.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios:
                print(usuario)

    # Empréstimos
    def realizar_emprestimo(self, id_usuario, codigo_livro):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        livro = next((l for l in self.livros if l.codigo == codigo_livro), None)

        if not usuario:
            print("Usuário não encontrado.")
            return
        if not livro:
            print("Livro não encontrado.")
            return

        self.emprestimos.append(Emprestimo(usuario, livro))
        print("Empréstimo registrado com sucesso.")

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Nenhum empréstimo registrado.")
        else:
            for e in self.emprestimos:
                print(e)

    # eBooks
    def cadastrar_ebook(self, codigo, titulo, autor, formato, preco):
        self.ebooks.append(Ebook(codigo, titulo, autor, formato, preco))
        print("eBook cadastrado com sucesso.")

    def listar_ebooks(self):
        if not self.ebooks:
            print("Nenhum eBook cadastrado.")
        else:
            for ebook in self.ebooks:
                print(ebook)

    def comprar_ebook(self, codigo):
        ebook = next((e for e in self.ebooks if e.codigo == codigo), None)
        if ebook:
            ebook.comprar()
        else:
            print("eBook não encontrado.")

    def baixar_ebook(self, codigo):
        ebook = next((e for e in self.ebooks if e.codigo == codigo), None)
        if ebook:
            ebook.fazer_download()
        else:
            print("eBook não encontrado.")


# ===== INTERFACE MENU =====
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== SISTEMA DA BIBLIOTECA =====")
        print("1. Cadastrar livro físico")
        print("2. Listar livros físicos")
        print("3. Cadastrar usuário")
        print("4. Listar usuários")
        print("5. Realizar empréstimo de livro")
        print("6. Listar empréstimos")
        print("7. Cadastrar eBook")
        print("8. Listar eBooks")
        print("9. Comprar eBook")
        print("10. Baixar eBook")
        print("0. Sair")
        print("=================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código do livro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de publicação: ")
            biblioteca.cadastrar_livro(codigo, titulo, autor, ano)

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            id_usuario = input("ID do usuário: ")
            nome = input("Nome: ")
            email = input("Email: ")
            biblioteca.cadastrar_usuario(id_usuario, nome, email)

        elif opcao == "4":
            biblioteca.listar_usuarios()

        elif opcao == "5":
            id_usuario = input("ID do usuário: ")
            codigo_livro = input("Código do livro: ")
            biblioteca.realizar_emprestimo(id_usuario, codigo_livro)

        elif opcao == "6":
            biblioteca.listar_emprestimos()

        elif opcao == "7":
            codigo = input("Código do eBook: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            formato = input("Formato (pdf, epub, etc): ")
            preco = float(input("Preço: R$"))
            biblioteca.cadastrar_ebook(codigo, titulo, autor, formato, preco)

        elif opcao == "8":
            biblioteca.listar_ebooks()

        elif opcao == "9":
            codigo = input("Código do eBook que deseja comprar: ")
            biblioteca.comprar_ebook(codigo)

        elif opcao == "10":
            codigo = input("Código do eBook que deseja baixar: ")
            biblioteca.baixar_ebook(codigo)

        elif opcao == "0":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# ===== EXECUTAR SISTEMA =====
if __name__ == "__main__":
    menu()

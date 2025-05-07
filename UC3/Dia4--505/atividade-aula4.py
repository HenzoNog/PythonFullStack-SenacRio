import os


def salvar_usuario(nome, email):
    with open('dados.txt', 'a') as arquivo:
        arquivo.write(f'{nome.lower()}, {email.lower()}\n')
    print("\nUsuário adicionado com sucesso!")


def listar_usuarios():
    if os.path.exists('dados.txt'):
        with open('dados.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
            if usuarios:
                print("\nLista de Usuários:")
                for usuario in usuarios:
                    nome, email = usuario.strip().split(', ')
                    print(f"Nome: {nome.capitalize()} | Email: {email}")
            else:
                print("\nNenhum usuário cadastrado.")
    else:
        print("\nO arquivo de dados não existe.")

def excluir_usuario(nome_ou_email):
    if os.path.exists('dados.txt'):
        with open('dados.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()

   
        usuario_encontrado = False
        for usuario in usuarios:
            if nome_ou_email.lower() in usuario.lower():
                usuarios.remove(usuario)
                usuario_encontrado = True
                break

        if usuario_encontrado:
            
            with open('dados.txt', 'w') as arquivo:
                arquivo.writelines(usuarios)
            print("\nUsuário excluído com sucesso!")
        else:
            print("\nUsuário não encontrado.")
    else:
        print("\nO arquivo de dados não existe.")


def main():
    while True:
        print("\nMenu:")
        print("1 - Adicionar novo usuário")
        print("2 - Listar todos os usuários")
        print("3 - Excluir usuário")
        print("4 - Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ").strip()

        if escolha == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            salvar_usuario(nome, email)

        elif escolha == '2':
            listar_usuarios()

        elif escolha == '3':
            nome_ou_email = input("Digite o nome ou email do usuário a excluir: ")
            excluir_usuario(nome_ou_email)

        elif escolha == '4':
            print("\nSaindo do programa.")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

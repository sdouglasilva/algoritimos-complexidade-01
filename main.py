from services.user_service import create_user, list_users

def main():
    while True:
        print("\n1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            print(create_user(nome, email))
        elif opcao == "2":
            print("\nLista de Usuários:")
            print(list_users())
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

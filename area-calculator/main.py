from services.user_service import create_user, list_users
from services.area_service import calcular_area_retangulo, calcular_area_circulo, calcular_area_triangulo

def main():
    while True:
        print("\n1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Calcular Áreas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            print(create_user(nome, email))
        elif opcao == "2":
            print("\nLista de Usuários:")
            print(list_users())
        elif opcao == "3":
            print("\nCalculando Áreas...")
            # Usando as sub-rotinas para calcular as áreas
            base_retangulo = 5
            altura_retangulo = 10
            area_retangulo = calcular_area_retangulo(base_retangulo, altura_retangulo)
            print(f"Área do retângulo: {area_retangulo} unidades quadradas")

            raio_circulo = 7
            area_circulo = calcular_area_circulo(raio_circulo)
            print(f"Área do círculo: {area_circulo} unidades quadradas")

            base_triangulo = 6
            altura_triangulo = 8
            area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
            print(f"Área do triângulo: {area_triangulo} unidades quadradas")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

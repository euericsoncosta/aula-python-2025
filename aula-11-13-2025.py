#cadastro de animais em petshop 
# 1 - criar menu para cadastrar, listar, doar e sair
# 2 - criar lista para armazenar os animais
# 3 - criar funcoes para cada opcao do menu


def cadastrar_animal(lista_de_animais):
    # nome_animal = input("Digite o nome do animal: ")
    # animais.append(nome_animal)
    lista_de_animais.append(input("Digite o nome do animal: "))
    print("Animal cadastrado com sucesso!")


def listar_animais(lista_de_animais):
    # if not lista_de_animais:
    #     print("Nenhum animal cadastrado.")
    if len(lista_de_animais) == 0:
        print("Nenhum animal cadastrado.")
    else:
        print("Lista de animais cadastrados: ")
        for animal in lista_de_animais:
            print(f"Animal: {animal}")
    
def doar_animal(lista_de_animais):
    nome_animal = input("Digite o nome do animal o qual você deseja doar: ")
    animal_encontrado = False
    for animal in lista_de_animais:
        if animal == nome_animal:
            lista_de_animais.remove(animal)
            print("Animal doado com sucesso!")
            animal_encontrado = True

    if animal_encontrado == False:
        print("Animal não encontrado na lista.")


def exibir_menu():
    print("----- Menu -----")
    print("1 - Cadastrar animal")
    print("2 - Listar animais")
    print("3 - Doar animal")
    print("4 - Sair")
    print("----------------")


def programa_principal():
    lista_de_animais = []
    opcao = 0
    while opcao != 4:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            cadastrar_animal(lista_de_animais)
        elif opcao == 2:
            listar_animais(lista_de_animais)
        elif opcao == 3:
            doar_animal(lista_de_animais)
        elif opcao == 4:
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")


programa_principal()

    
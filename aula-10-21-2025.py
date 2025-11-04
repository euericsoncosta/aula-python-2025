#estudo sobre listas em Python
# minha_lista = ["Banana", "maçã", "Abacaxi", "Laranja"]#criar uma lista com frutas

# print(minha_lista[0])
# print(minha_lista[1])#imprimir o segundo item da lista

# print(minha_lista[2])#imprimir o terceiro item da lista

# for fruta in minha_lista:#imprimir todas as frutas
#     print(fruta)


# print(len(minha_lista))#imprimir o tamanho da lista

# tamanho_lista = len(minha_lista)#armazenar o tamanho da lista em uma variável
# print(f"O tamanho da lista é:{tamanho_lista}")#imprimir o tamanho da lista armazenado


# minha_lista.append("Uva")#adicionar uma fruta na lista

# minha_lista.pop()#remover o último item da lista

# item_removido = minha_lista.pop()#remover o último item da lista e armazenar em uma variável


#programa cadastro e remocao de itens em uma lista


def exibir_menu():
    print("Menu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir itens")
    print("4. Sair")
    escolha = int(input("Escolha uma opção (1-4): "))
    return escolha


def main():
    lista_itens = []
    opcao = 0
    while opcao != 4:
        opcao = exibir_menu()
        if opcao == 1:
            item = input("Digite o item a ser adicionado: ")
            lista_itens.append(item)
            print(f"Item '{item}' adicionado.")
        elif opcao == 2:
            item = input("Digite o item a ser removido: ")
            if item in lista_itens:
                lista_itens.remove(item)
                print(f"Item '{item}' removido.")
            else:
                print(f"Item '{item}' não encontrado na lista.")
        elif opcao == 3:
            print("Itens na lista:")
            for item in lista_itens:
                print(f"- {item}")
        else:
            print("Saindo do programa.")


main()  
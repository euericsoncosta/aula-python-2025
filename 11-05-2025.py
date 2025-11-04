def mostrar_menu():
    print("Menu de opções:")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

def adicionar_tarefa(lista_de_tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    lista_de_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def ver_tarefas(lista_de_tarefas):
    if len(lista_de_tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas cadastradas:")
        for i, tarefa in enumerate(lista_de_tarefas):
            print(f"{i + 1} - {tarefa}")

def remover_tarefa(lista_de_tarefas):
    if len(lista_de_tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        ver_tarefas(lista_de_tarefas)
        escolha = int(input("Digite o número da tarefa a ser removida: "))
        tarefa_removida = lista_de_tarefas.pop(escolha - 1)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    

def principal():
    tarefas = []
    opcao = 0
    while opcao != 4:
        mostrar_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_tarefa(tarefas)
        elif opcao == 2:
            ver_tarefas(tarefas)
        elif opcao == 3:
            remover_tarefa(tarefas)
        elif opcao == 4:
            print("Saindo do sistema.")
        else:
            print("Opção inválida. Tente novamente.")


principal()
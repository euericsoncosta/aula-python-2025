def mostrar_menu():#cria o menu de opções
    print("Menu de opções:")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

def adicionar_tarefa(lista_de_tarefas):#adiciona uma tarefa na lista
    tarefa = input("Digite a tarefa a ser adicionada: ")#pergunta a tarefa
    lista_de_tarefas.append(tarefa)#adiciona a tarefa na lista
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")#confirma a adição da tarefa

def ver_tarefas(lista_de_tarefas):#mostra as tarefas cadastradas
    if len(lista_de_tarefas) == 0:#verifica se a lista está vazia
        print("Nenhuma tarefa cadastrada.")#informa que não há tarefas
    else:#se houver tarefas
        print("Tarefas cadastradas:")#mostra as tarefas
        for i, tarefa in enumerate(lista_de_tarefas):#percorre a lista de tarefas
            print(f"{i + 1} - {tarefa}")#imprime a tarefa com seu número

def remover_tarefa(lista_de_tarefas):#remove uma tarefa da lista
    if len(lista_de_tarefas) == 0:#verifica se a lista está vazia
        print("Nenhuma tarefa cadastrada.")#informa que não há tarefas
    else:#se houver tarefas
        ver_tarefas(lista_de_tarefas)#mostra as tarefas cadastradas
        escolha = int(input("Digite o número da tarefa a ser removida: "))#pergunta qual tarefa remover
        tarefa_removida = lista_de_tarefas.pop(escolha - 1)#remove a tarefa da lista
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")#confirma a remoção da tarefa
    

def principal():#função principal do programa
    tarefas = []#lista de tarefas vazia
    opcao = 0#variável para armazenar a opção do menu
    while opcao != 4:#enquanto a opção não for sair
        mostrar_menu()#mostra o menu de opções
        opcao = int(input("Escolha uma opção: "))#pergunta a opção do usuário
        if opcao == 1:#se a opção for adicionar tarefa
            adicionar_tarefa(tarefas)#chama a função para adicionar tarefa
        elif opcao == 2:#se a opção for ver tarefas
            ver_tarefas(tarefas)#chama a função para ver tarefas
        elif opcao == 3:#se a opção for remover tarefa
            remover_tarefa(tarefas)#chama a função para remover tarefa
        elif opcao == 4:#se a opção for sair
            print("Saindo do sistema.")#informa que está saindo
        else:#se a opção for inválida
            print("Opção inválida. Tente novamente.")#informa que a opção é inválida


principal()#chama a função principal para iniciar o programa
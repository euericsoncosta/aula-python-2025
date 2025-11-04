#sistema de cadastro e chamados em uma clinica

pacientes = []
opcao = 0
while opcao != 4:
    # if len(pacientes) == 0:
    #     print("\nNenhum paciente cadastrado.")
    # else:
    #     print("\nPacientes cadastrados:")
    #     for i, paciente in enumerate(pacientes):
    #         print(f"{i + 1} - {paciente}")
    print("\nMenu:")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Pacientes")
    print("3 - Chamar paciente para consulta")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do Paciente: ")
        pacientes.append(nome)
        print(f"Paciente {nome} cadastrado com sucesso!")
    elif opcao == 2:
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            for i, paciente in enumerate(pacientes):
                print(f"{i + 1} - {paciente}")
    elif opcao == 3:
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            escolha = int(input("Digite o número do paciente a ser chamado: "))
            paciente_chamado = pacientes.pop(escolha - 1)
            print(f"Paciente {paciente_chamado} chamado para consulta.")
    elif opcao == 4:
        print("Saindo do sistema.")


    
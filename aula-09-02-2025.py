#estrutura de controle if, else e elif

# if = se
# else = senão
# elif = senão se

# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print("O número é par")
# else:
#     print("O número é ímpar")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

    
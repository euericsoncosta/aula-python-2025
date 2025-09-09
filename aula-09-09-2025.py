# #Sistema de calculo de IMC


# print(" Calculadora de IMC ")
# peso = float(input("Digite seu peso em kg: "))
# #float para aceitar números decimais
# altura = float(input("Digite sua altura em metros: "))

# imc = peso / (altura ** 2)

# print(f"Seu IMC é: {imc:.2f}")

# if imc < 18.5:
#     print("Você está abaixo do peso.")
# elif 18.5 <= imc and imc <= 24.9:
#     print("Você está com o peso normal.")
# elif 25 <= imc and imc <= 29.9:
#     print("Você está com sobrepeso.")
# elif 30 <= imc and imc <= 34.9:
#     print("Você está com obesidade grau 1.")
# elif 35 <= imc and imc <= 39.9:
#     print("Você está com obesidade grau 2.")
# else:
#     print("Você está com obesidade grau 3.")




#verificar o maior numero de 3 números

n1 = int(input("Digite o primeiro número: "))
#int para aceitar apenas números inteiros
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"O maior número é {n1}, o segundo maior é {n2} e o menor é {n3}")   
    else:
        print(f"O maior número é {n1}, o segundo maior é {n3} e o menor é {n2}")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"O maior número é {n2}, o segundo maior é {n1} e o menor é {n3}")
    else:
        print(f"O maior número é {n2}, o segundo maior é {n3} e o menor é {n1}")
else:
    if n1 > n2:
        print(f"O maior número é {n3}, o segundo maior é {n1} e o menor é {n2}")
    else:
        print(f"O maior número é {n3}, o segundo maior é {n2} e o menor é {n1}")


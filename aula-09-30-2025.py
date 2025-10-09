



# def calculo_imc(peso, altura):
#     imc = peso / (altura * altura)
#     return imc

# def classificar_imc(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif 18.5 <= imc and imc < 24.9:
#         return "Peso normal"
#     elif imc>=25 and imc <= 29.9:
#         return "Sobrepeso"
#     else:
#         return "Obesidade"
    





# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura: "))

# imc = calculo_imc(peso, altura)
# classificacao = classificar_imc(imc)

# print(f"Seu IMC é: {imc:.2f}")
# print(f"Sua classificação é: {classificacao}")





# def soma_numeros(n):
#     if n == 1:
#         return 1
#     else:
#         return n + soma_numeros(n - 1)


# print(soma_numeros(5))
def jogo_adivinhacao():
    numero_secreto = 7
    tentativa = 0

    while tentativa != numero_secreto:
        tentativa = int(input("Adivinhe o número secreto"))
        if tentativa == numero_secreto:
            print("Parabéns! Você acertou!")
        else:
            print("Tente novamente.")


def contagem_regressiva(n):
    for i in range(n, 0, -1):#n: onde a contagem começa, 0: onde a contagem termina, -1: de quanto em quanto a contagem diminui
        print(i)



contagem_regressiva(5)




import random 
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 50) #numero aleatorio entre 1 e 50
    numero_escolhido = 0 #numero escolhido pelo usuario
    tentativas = 0 #contador de tentativas

    while numero_escolhido != numero_secreto: #enquanto o numero escolhido for diferente do numero secreto

        numero_escolhido = int(input("Digite um numero de 1 a 50: "))#pede para o usuario digitar um numero
        tentativas += 1#incrementa o contador de tentativas
        if numero_escolhido < numero_secreto:#se o numero escolhido for menor que o numero secreto
            print("Tente um numero maior")#se o numero escolhido for maior que o numero secreto
        elif numero_escolhido > numero_secreto:#se o numero escolhido for maior que o numero secreto
            print("Tente um numero menor")
        else:#se o numero escolhido for igual ao numero secreto
            print(f"Parabens! Voce acertou o numero {numero_secreto} em {tentativas} tentativas.")#imprime a mensagem de acerto

def calculadora_imc():
    def calculo_imc(peso, altura):
        imc = peso / (altura * altura)
        return imc

    def classificar_imc(imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc and imc < 24.9:
            return "Peso normal"
        elif imc>=25 and imc <= 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = calculo_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Sua classificação é: {classificacao}")


    for i in range(n, 0, -1):#n: onde a contagem começa, 0: onde a contagem termina, -1: de quanto em quanto a contagem diminui
        print(i)
    print("Fogo!")

def menu_inicial():
    escolha = 0


    print("Menu Inicial")
    print("1 - Jogo de Adivinhação")
    print("2 - Calculadora de IMC")
    print("3 - Sair")

    escolha = int(input("Escolha uma opção: "))
        
    return escolha

def programa_principal():
    numero_escolhido = 0

    while numero_escolhido != 3:
        numero_escolhido = menu_inicial()

        if numero_escolhido == 1:
            jogo_adivinhacao()
        elif numero_escolhido == 2:
            calculadora_imc()
        elif numero_escolhido == 3:
            print("Saindo...")


programa_principal()
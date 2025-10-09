#funções em python. funcionamento

# def saudacao():
#     print("Olá, seja bem-vindo!")
#     print("Espero que você tenha um ótimo dia!")

# saudacao()
# saudacao()
# saudacao()
# saudacao()



# def somar(a,b):
#     print(a + b)



# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# somar(num1, num2)

def calculoIMC(peso, altura):
    imc = peso /(altura * altura)
    print(f"Seu IMC é: {imc}")


    

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

calculoIMC(peso, altura)

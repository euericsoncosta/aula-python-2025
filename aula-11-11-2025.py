#correção atividade anterior
#  Exercício 13:

# ✔ Faça um programa que tenha uma função chamada contador(), que
# receba três parâmetros: início, fim e passo. Seu programa tem que
# realizar três contagens através da função criada:

# def contador(inicio, fim, passo):
#     if inicio < fim:
#         for i in range(inicio, fim + 1, passo):
#             print(i)
#     elif inicio > fim:
#         for i in range(inicio, fim -1, -passo):
#             print(i)

# # Primeira contagem
# def contagem():
#     inicio  = int(input("Digite o início da contagem: "))
#     fim     = int(input("Digite o fim da contagem: "))
#     passo   = int(input("Digite o passo da contagem: "))

#     contador(inicio, fim, passo)


# contagem()


# Exercício 14:

# ✔ Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

# def maior(numeros):
#     maior_numero = max(numeros)
#     return maior_numero

# def maior_numero():
#     numeros = []
#     numero = 1
#     while numero != 0:#! = diferente
#         numero = int(input("Digite um número inteiro (ou 0 para sair): "))
#         numeros.append(numero)

#     if len(numeros) > 1:
#         print(f"O maior número digitado foi: {maior(numeros)}")


# maior_numero()


# Exercício 15:

# ✔ Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.

# import random
# import math

# def sorteia(lista):
#     for i in range(5):
#         numero = random.randint(1, 1000)
#         lista.append(numero)
#     print(f"Números sorteados:{lista}")

# def somaPar(lista):
#     soma = 0
#     for numero in lista:
#         if numero % 2 == 0:
#             soma += numero
#     print(f"Soma dos números pares: {soma}")


# def sortear_e_somar():
#     numeros = []
#     sorteia(numeros)
#     somaPar(numeros)


# sortear_e_somar()


# Exercício 16:

# ✔ Crie um programa que tenha uma função fatorial() e retorno o valor fatorial
# de três variáveis em tela.

# def fatorial(x):# funcao fatorial
#     fatorial = 1 # inicializa fatorial com 1
#     if x == 0 or x ==1:# condição para 0! e 1!
#         return 1 #retorna 1
#     else:# para outros valores
#         for i in range(x, 0, -1):# loop decrescente de x até 1
#             # fatorial = fatorial * i # calcula o fatorial
#             fatorial *= i # calcula o fatorial
#     return fatorial # retorna o valor do fatorial

# def calcular_fatoriais():# calcula fatoriais de 3 números
#     numeros =[]# lista para armazenar os números
#     for i in range(3):# loop para 3 números
#         numero = int(input(f"Digite o {i+1}º número para calcular o fatorial: "))
#         numeros.append(numero)# adiciona o número à lista
#     for numero in numeros:# loop para calcular e exibir o fatorial de cada número
#         print(f"O fatorial de {numero} é {fatorial(numero)}")# exibe o fatorial

# calcular_fatoriais()# chama a função para calcular os fatoriais


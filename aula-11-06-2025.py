#Faça um programa que tenha uma função chamada área(), que receba as
#dimensões de um terreno retangular (largura e comprimento) e mostre a
#área do terreno.
# Exercício 12:

# ✔ Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a
# área do terreno.

# def area(largura, comprimento):
#     area_terreno = largura * comprimento
#     return area_terreno


# def calcular_area_terreno():

#     largura = float(input("Digite a largura do terreno em metros: "))
#     comprimento = float(input("Digite o comprimento do terreno em metros: "))

#     resultado = area(largura, comprimento)

#     print(f"A area do terreno é: {area(largura, comprimento) } metros quadrados.")
#     print(f"A area do terreno é: {resultado} metros quadrados.")


# calcular_area_terreno()


# Exercício 13:

# ✔ Faça um programa que tenha uma função chamada contador(), que
# receba três parâmetros: início, fim e passo. Seu programa tem que
# realizar três contagens através da função criada:

# def contador(inicio, fim, passo):
#     if inicio < fim:
#         for i in range(inicio, fim + 1, passo):#inclusive o fim
#             print(i, end=' ')#mostra na mesma linha
#     else:

#         for i in range(inicio, fim - 1, -passo):#inclusive o fim
#             print(i, end=' ')#mostra na mesma linha

# inicio = int(input("Digite o início da contagem: "))
# fim = int(input("Digite o fim da contagem: "))
# passo = int(input("Digite o passo da contagem: "))
# contador(inicio, fim, passo)


# Exercício 14:

# ✔ Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

# def maior(numeros):
#     maior_numero = max(numeros)
#     return maior_numero

# numero = 1
# numeros = []
# while numero != 0:
#     numero = int(input("Digite um número inteiro (0 para parar): "))
#     numeros.append(numero)
    
# if len(numeros) > 1:
#     maior(numeros)
#     print(f"O maior número digitado foi: {maior(numeros)}")
# else:
#     print("Nenhum número foi digitado.")

# Exercício 15:

# ✔ Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.


# import random
# import math
# def sorteia(lista):
#     for i in range(5):
#         numero = random.randint(1, 100)
#         lista.append(numero)
#     print("Números sorteados:", lista)

# def somaPar(lista):
#     soma = 0
#     for numero in lista:
#         if numero % 2 == 0:
#             soma += numero
#     print("Soma dos números pares:", soma)

# def sortear_e_somar():
#     numeros = []
#     sorteia(numeros)
#     somaPar(numeros)

# sortear_e_somar()


# Exercício 16:

# ✔ Crie um programa que tenha uma função fatorial() e retorno o valor fatorial
# de três variáveis em tela.

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
# def calcular_fatoriais():
#     numeros = []
#     for i in range(3):
#         numero = int(input(f"Digite o {i+1}º número para calcular o fatorial: "))
#         numeros.append(numero)
    
#     for numero in numeros:
#         print(f"O fatorial de {numero} é {fatorial(numero)}")   

# Exercício 17:

# ✔ Crie um programa que tenha uma função par() e verifique se o número
# digitado é par ou não.

# def par(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False    
    
# def verificar_numero_par():
#     numero = int(input("Digite um número inteiro: "))
#     if par(numero):
#         print(f"O número {numero} é par.")
#     else:
#         print(f"O número {numero} não é par.")

# verificar_numero_par()

# Exercício 18:

# ✔ Faça um programa, com uma função que necessite de um argumento. A
# função retorna o valor de caractere ‘P’, se seu argumento for positivo, e
# ‘N’, se seu argumento for zero ou negativo.

# def verificar_positivo_negativo(n):
#     if n > 0:
#         return 'P'
#     else:
#         return 'N'
# def checar_numero():
#     numero = float(input("Digite um número: "))
#     resultado = verificar_positivo_negativo(numero)
#     if resultado == 'P':
#         print(f"O número {numero} é positivo.")
#     else:
#         print(f"O número {numero} é zero ou negativo.")
# checar_numero()


# Exercício 19:

# ✔ Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o
# imposto sobre vendas.

# def somaImposto(taxaImposto, custo):
#     custo_com_imposto = custo + (custo * taxaImposto / 100)
#     return custo_com_imposto

# def calcular_custo_com_imposto():
#     taxaImposto = float(input("Digite a taxa de imposto sobre vendas (em %): "))
#     custo = float(input("Digite o custo do item antes do imposto: "))

#     custo_final = somaImposto(taxaImposto, custo)

#     print(f"O custo do item após o imposto é: R$ {custo_final:.2f}")

# calcular_custo_com_imposto()

# Exercício 20:

# ✔ Faça um programa que converta da notação de 24 horas para a notação de 12
# horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada
# é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer
# a conversão e uma para a saída. Registre a informação A.M./P.M. como um
# valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões
# terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que
# permita que o usuário repita esse cálculo para novos valores de entrada todas
# as vezes que desejar.

# def converter_para_12_horas(hora_24):
#     if hora_24 == 0:
#         return 12, 'A'
#     elif hora_24 < 12:
#         return hora_24, 'A' 
#     elif hora_24 == 12:
#         return 12, 'P'
#     else:
#         return hora_24 - 12, 'P'
# def exibir_hora(hora_12, periodo):
#     print(f"A hora convertida é: {hora_12}:00 {periodo}.M.")

# def main():
#     while True:
#         hora_24 = int(input("Digite a hora em notação de 24 horas (0-23): "))
#         if 0 <= hora_24 <= 23:
#             hora_12, periodo = converter_para_12_horas(hora_24)
#             exibir_hora(hora_12, periodo)
#         else:
#             print("Hora inválida. Por favor, digite um valor entre 0 e 23.")
        
#         repetir = input("Deseja converter outra hora? (s/n): ").lower()
#         if repetir != 's':
#             break
# main()





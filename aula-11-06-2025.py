#Faça um programa que tenha uma função chamada área(), que receba as
#dimensões de um terreno retangular (largura e comprimento) e mostre a
#área do terreno.


def area(largura, comprimento):
    area_terreno = largura * comprimento
    return area_terreno


def calcular_area_terreno():

    largura = float(input("Digite a largura do terreno em metros: "))
    comprimento = float(input("Digite o comprimento do terreno em metros: "))

    resultado = area(largura, comprimento)

    print(f"A area do terreno é: {area(largura, comprimento) } metros quadrados.")
    print(f"A area do terreno é: {resultado} metros quadrados.")


calcular_area_terreno()
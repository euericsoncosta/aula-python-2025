#  Escreva um programa que use um for para imprimir os números de 1 a 10.
for i in range(1, 11):  # percorre os numeros de 1 a 10
    print(i)  # imprime o numero atual

#  Faça um programa com while que mostre os números de 10 até 1 e, ao final, exiba “Fogo!”.

contador = 10  # inicializa o contador com 10
while contador >= 1:  # enquanto o contador for maior ou igual a 1
    print(contador)  # imprime o valor atual do contador
    contador -= 1  # decrementa o contador em 1

print("Fogo!")  # imprime "Fogo!" após o loop

#  Peça ao usuário 5 números inteiros e use um for para calcular e mostrar a soma total.

soma = 0  # inicializa a soma com 0
for i in range(5):  # repete 5 vezes    
    num = int(input("Digite um número inteiro: "))  # pede ao usuario para digitar um numero inteiro
    soma += num  # adiciona o numero digitado à soma
print(f"A soma total é: {soma}")  # imprime a soma total

# Solicite ao usuário um número e mostre a tabuada desse número (1 a 10) usando for.

num = int(input("Digite um número para ver sua tabuada: "))  # pede ao usuario para digitar um numero e converte para inteiro
for i in range(1, 11):  # percorre os numeros de 1 a 10
    print(f"{num} x {i} = {num * i}")  # imprime a tabuada do numero digitado

#  Peça um nome e um número n. Mostre o nome digitado n vezes usando um for.

nome = input("Digite um nome: ")  # pede ao usuario para digitar um nome
n = int(input("Digite um número: "))  # pede ao usuario para digitar um numero e converte para inteiro
for i in range(n):  # repete n vezes
    print(nome)  # imprime o nome digitado


# Faça um programa que leia vários números e some todos, até que o usuário digite 0.
soma = 0  # inicializa a soma com 0
valor_digitado = None  # inicializa a variável para armazenar o valor digitado
while valor_digitado != 0:
    valor_digitado = int(input("Digite um número (0 para sair): "))  # pede ao usuario para digitar um numero e converte para inteiro
    soma += valor_digitado  # adiciona o numero digitado à soma

print(f"A soma total é: {soma}")  # imprime a soma total

# Peça as notas de 4 alunos e mostre a média da turma usando um for.
media = 0  # inicializa a média com 0
num_notas = 4
for i in range(num_notas):  # repete 4 vezes
    nota = float(input(f"Digite a nota numero: {i + 1}: "))  # pede ao usuario para digitar a nota  e converte para float
    media += nota  # adiciona a nota à média

media /= num_notas  # calcula a média dividindo pela quantidade de notas
print(f"A média da turma é: {media}")  # imprime a média da turma

# Peça um número e use for para verificar se ele é primo.
num = int(input("Digite um número para verificar se é primo: "))  # pede ao usuario para digitar um numero e converte para inteiro
eh_primo = True  # inicializa a variável para verificar se é primo
for i in range(2, int(num**0.5) + 1):  # percorre os numeros de 2 até a raiz quadrada do numero
    if num % i == 0:  # se o numero for divisível por i
        eh_primo = False  # não é primo
        break  # sai do loop
if eh_primo and num > 1:  # verifica se é primo e maior que 1
    print(f"{num} é um número primo.")  # imprime que é primo
else:
    print(f"{num} não é um número primo.")  # imprime que não é primo

# Peça um número e mostre o seu fatorial usando um for.
num = int(input("Digite um número para calcular o fatorial: "))  # pede ao usuario para digitar um numero e converte para inteiro
fatorial = 1  # inicializa o fatorial com 1
for i in range(num, 0, -1):  # percorre os numeros de 1 até o numero
    fatorial *= i  # multiplica o fatorial pelo numero atual
print(f"O fatorial de {num} é: {fatorial}")  # imprime o










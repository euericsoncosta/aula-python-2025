#operadores de atribuição
# =, +=, -=, *=, /=, //=, **=, %=

# numero = 2 
# print(f" primeiro: {numero}")
# numero1 = 3 

# numero = numero + 3 
# print(f" somei 3: {numero}")
# numero += 3 # mesma coisa que numero = numero + 3
# print(f" somei 3 de novo: {numero}")
# numero = numero * 2 
# print(f" multipliquei por 2: {numero}")
# numero *= 2 # mesma coisa que numero = numero * 2
# print(f" multipliquei por 2 de novo: {numero}")
# numero = numero - 4 
# print(f" subtrai 4: {numero}")
# numero -= 4 # mesma coisa que numero = numero - 4
# print(f" subtrai 4 de novo: {numero}")

# idade = 25
# tem_carteira = True
# e_feriado = False

# pode_dirigir = idade >= 18 and tem_carteira
# print(pode_dirigir)
# pode_descansar = e_feriado or idade >65
# print(pode_descansar)





idade = int(input("Digite sua idade: "))
tem_carteira = input("Você tem carteira de motorista? (s/n): ") == "s"
pode_dirigir = idade >= 18 and tem_carteira

print(f"Pode dirigir: {pode_dirigir}")





#estudo sobre listas em Python
minha_lista = ["Banana", "maçã", "Abacaxi", "Laranja"]#criar uma lista com frutas

print(minha_lista[0])
print(minha_lista[1])#imprimir o segundo item da lista

print(minha_lista[2])#imprimir o terceiro item da lista

for fruta in minha_lista:#imprimir todas as frutas
    print(fruta)


print(len(minha_lista))#imprimir o tamanho da lista

tamanho_lista = len(minha_lista)#armazenar o tamanho da lista em uma variável
print(f"O tamanho da lista é:{tamanho_lista}")#imprimir o tamanho da lista armazenado


minha_lista.append("Uva")#adicionar uma fruta na lista

minha_lista.pop()#remover o último item da lista

item_removido = minha_lista.pop()#remover o último item da lista e armazenar em uma variável

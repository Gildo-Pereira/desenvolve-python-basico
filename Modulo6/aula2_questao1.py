import random
lista=[]

for i in range(20):
    numero = random.randint(-100, 100)
    lista.append(numero)
print(f"Lista ordenada{sorted(lista)}")
print(f"Lista original: {lista}")
print(f"Índice do maior valor {lista.index(max(lista))}")
print(f"Índice do menor valor {lista.index(min(lista))}")
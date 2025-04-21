import random
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)
inicio_maior, tamalho_maior,inicio_atual, tamalho_atual=0,0,0,0
for i in range(len(lista)):
    if lista[i]<0:
        tamalho_atual+=1
        if tamalho_atual==1:
            inicio_atual= i
    else:
        if tamalho_atual> tamalho_maior:
            tamalho_maior=tamalho_atual
            inicio_maior=inicio_atual
        tamalho_atual=0
del lista[inicio_maior:inicio_maior+tamalho_maior]
print("Lista editada:", lista)
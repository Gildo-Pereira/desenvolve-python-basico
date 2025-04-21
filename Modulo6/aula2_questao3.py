import random
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = sorted(set(lista1) & set(lista2))
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseccao:", interseccao)
print("\nContagem")
for valor in interseccao:
    count1 = lista1.count(valor)
    count2 = lista2.count(valor)
    print(f"{valor}: (lista1={count1}, lista2={count2})")


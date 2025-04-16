import random
import math
n = int(input("Digite a quantidade de números aleatórios: "))
soma = 0
for i in range(n):
    numero = random.randint(0, 100)
    print(f"Número gerado: {numero}")
    soma += numero
raiz = math.sqrt(soma)
print(f"A raiz quadrada da soma dos {n} numeros gerados é: {raiz:.2f}")
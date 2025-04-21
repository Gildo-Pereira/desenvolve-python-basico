# 1. Todos os números pares entre 20 e 50
pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]

# 2. Os quadrados dos valores de 1 a 9
quadrados = [x**2 for x in range(1,10)]

# 3. Números entre 1 e 100 divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

# 4. "par" ou "ímpar" para valores em range(0, 30, 3)
par_ou_impar = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]

# Impressão das listas
print("1. Pares de 20 a 50:", pares_20_50)
print("2. Quadrados:", quadrados)
print("3. Divisíveis por 7:", divisiveis_por_7)
print("4. Paridade de range(0,30,3):", par_ou_impar)

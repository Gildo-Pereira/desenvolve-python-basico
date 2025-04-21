# Lista para armazenar os valores
numeros = []

print("Digite números inteiros (digite 'fim' para encerrar):")

# Laço para entrada dos números
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        if len(numeros) < 4:
            print("Você precisa digitar pelo menos 4 números.")
            continue
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Digite apenas números inteiros ou 'fim' para encerrar.")

# Fatiamentos e exibições
print("\nLista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])

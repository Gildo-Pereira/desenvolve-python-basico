nome1 = input(f"Digite o nome do produto 1:")
preco1 = float(input(f"Digite o preço unitário do produto 1:"))
quantidade1 = int(input(f"Digite a quantidade do produto 1:"))
nome2 = input(f"Digite o nome do produto 2:")
preco2 = float(input(f"Digite o preço unitário do produto 2:"))
quantidade2 = int(input(f"Digite a quantidade do produto 2:"))
nome3 = input(f"Digite o nome do produto 3:")
preco3 = float(input(f"Digite o preço unitário do produto 3:"))
quantidade3 = int(input(f"Digite a quantidade do produto 3:"))
total = preco1 * quantidade1 + preco2 * quantidade2 + preco3 * quantidade3

# Impressão do total formatado

print (f"Total R$: {total:,.2f}")

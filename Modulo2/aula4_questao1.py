# Leitura do comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno (em metros): "))
# Leitura da largura do terreno
largura = int(input("Digite a largura do terreno (em metros): "))
# Leitura do preço do metro quadrado
preco = float(input("Digite o preço do metro quadrado (em R$): "))
# Cálculo da área e do valor do terreno
area = comprimento * largura
valor_total = area * preco
# Impressão do resultado formatado
print(f"O terreno possui {area}m2 e custa R${valor_total:,.2f}")
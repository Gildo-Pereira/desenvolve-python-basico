import re

# Abre o arquivo para leitura
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# 1. Exibir as primeiras 25 linhas
print("=== Primeiras 25 linhas ===\n")
for linha in linhas[:25]:
    print(linha.strip())

# 2. Número total de linhas
num_linhas = len(linhas)
print(f"\n=== Número total de linhas: {num_linhas} ===")

# 3. Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print("\n=== Linha com maior número de caracteres ===")
print(linha_maior.strip())
print(f"(comprimento: {len(linha_maior.strip())} caracteres)")

# 4. Contar menções a "Nonato" e "Íria" (ignorando maiúsculas/minúsculas e variações)
# Use regex para encontrar a palavra exata, ignorando se faz parte de outras palavras
texto_completo = ''.join(linhas)

# Conta ocorrências com palavra isolada (usando \b para bordas de palavra)
nonato_count = len(re.findall(r'\bnonato\b', texto_completo, re.IGNORECASE))
iria_count = len(re.findall(r'\bíria\b', texto_completo, re.IGNORECASE))

print(f"\n=== Contagem de nomes ===")
print(f"Menções a 'Nonato': {nonato_count}")
print(f"Menções a 'Íria': {iria_count}")

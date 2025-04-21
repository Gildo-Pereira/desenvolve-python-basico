# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais_lista = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Compreensão de listas
vogais = sorted(set([x for x in frase if x in vogais_lista]))
consoantes = list(set([x for x in frase if x.isalpha() and x not in vogais_lista]))

# Imprime os resultados
print("\nVogais:", vogais)
print("Consoantes:", consoantes)


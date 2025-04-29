#implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou".Exemplo:
#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
#19 vogais
#Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
indices_vogais = []
for i, caractere in enumerate(frase):
    if caractere in vogais:
        indices_vogais.append(i)
print(f"{len(indices_vogais)} vogais")
print("Índices", indices_vogais)
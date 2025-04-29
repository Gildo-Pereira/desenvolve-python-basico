#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
#Digite a palavra objetivo: amor
#Anagramas: ["amor", "mora", "ramo", "Roma"] 

def encontrar_anagramas(frase, palavra_objetivo):
    # Convertendo a frase em uma lista de palavras, removendo pontuação e deixando tudo em minúsculas
    import re
    palavras = re.findall(r'\b\w+\b', frase.lower())
    palavra_objetivo = palavra_objetivo.lower()
    caracteres_objetivo = sorted(palavra_objetivo)
    anagramas = []

    for palavra in palavras:
        if len(palavra) == len(palavra_objetivo):
            if sorted(palavra) == caracteres_objetivo:
                anagramas.append(palavra)
    return anagramas
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
resultado = encontrar_anagramas(frase, palavra_objetivo)
print("Anagramas:", resultado)
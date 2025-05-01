#Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada
#  palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
#Dica: use a biblioteca random.

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            meio = list(palavra[1:-1])  # letras internas
            random.shuffle(meio)       # embaralha as letras internas
            nova_palavra = palavra[0] + ''.join(meio) + palavra[-1]
            resultado.append(nova_palavra)

    return ' '.join(resultado)


frase = input("Digite uma frase: ")
resultado = embaralhar_palavras(frase)
print(resultado)

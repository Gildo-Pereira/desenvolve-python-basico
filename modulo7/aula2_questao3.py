#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco 
# ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".
#Digite uma frase (digite "fim" para encerrar): Radar
#"Radar" é palíndromo
#Digite uma frase (digite "fim" para encerrar): Bom dia!
#"Bom dia!" não é palíndromo
#Digite uma frase (digite "fim" para encerrar): Ame o poema
#"Ame o poema" é palíndromo
#Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
#"A Daniela ama a lei? Nada!" é palíndromo
#Digite uma frase (digite "fim" para encerrar): fim

import string

def palindromo(frase):
    # Remove espaços, pontuação e coloca tudo em minúsculo
    frase_limpa = ''.join(
        [char.lower() for char in frase if char.isalnum()]
    )
    # Verifica se é igual à sua versão invertida
    return frase_limpa == frase_limpa[::-1]

# Loop principal
while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    if entrada.strip().lower() == "fim":
        break

    if palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')

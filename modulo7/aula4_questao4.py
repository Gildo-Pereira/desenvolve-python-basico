import random

def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r") as file:
        estagios = file.read().split("\n\n")
    print(estagios[erros])

def jogo_da_forca():
    with open("gabarito_forca.txt", "r") as file:
        palavras = [linha.strip().lower() for linha in file.readlines()]
    palavra = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra]
    letras_usadas = set()
    erros = 4
    max_erros = 9

    print("Bem-vindo ao Jogo da Forca!")
    while erros <= max_erros and "_" in letras_descobertas:
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Letras usadas:", " ".join(sorted(letras_usadas)))
        letra = input("Digite uma letra: ").lower().strip()

        if not letra.isalpha() or len(letra) != 1:
            print("Digite apenas uma letra válida.")
            continue

        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Boa! Letra correta.")
        else:
            erros += 1
            print("Letra incorreta!")
            imprime_enforcado(erros)

    if "_" not in letras_descobertas:
        print("\nParabéns! Você acertou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

jogo_da_forca()

#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em 
# branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
import re

# Abrir o arquivo "frase.txt" e ler o conteúdo
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Extrair apenas palavras (letras), ignorando espaços, pontuação e números
palavras = re.findall(r'\b[a-zA-ZáéíóúãõâêîôûçÁÉÍÓÚÃÕÂÊÎÔÛÇ]+\b', conteudo)

# Salvar cada palavra em uma nova linha no arquivo "palavras.txt"
with open("palavras.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Ler e imprimir o conteúdo do arquivo "palavras.txt"
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    print("Conteúdo do arquivo palavras.txt:")
    print(arquivo.read())

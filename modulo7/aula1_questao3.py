#Escreva um script que dado uma frase conta os espaços em branco
frase = input("Digite a frase: ")
espaco=0
for i in range(len(frase)):
    if frase[i] == " ":
        espaco+=1
print("Espaços em branco: ", espaco)
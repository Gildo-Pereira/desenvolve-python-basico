#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
#Digite uma frase: O rato roeu a roupa do rei
#frase modificada: * r*t* r*** * r**p* d* r**

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_modificada = ''.join(['*' if char in vogais else char for char in frase])
print("Frase modificada:", frase_modificada)

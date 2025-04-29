#Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.
nome = input("Digite seu primeiro nome: ")
sobre_nome=input("Digite seu sobrenome: ")
print(f"Bem-vindo (a), {nome + " " + sobre_nome}!")
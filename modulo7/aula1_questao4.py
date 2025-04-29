#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já 
#tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
numero = input("Digite o número: ")
numeroC=0
if len(numero) == 8: 
    numero = "9" + numero
    for i in range(0,6):
        numeroC=numero[:i]
        i+=1
    numeroC += "-"
    for i in range(5,9):
        numeroC+=numero[i]
        i+=1
    print("Número completo: ", numeroC)
elif len(numero) == 9:
    if numero[0] == "9":
        for i in range(0,6):
            numeroC= numero[:i]
            i+=1
        numeroC += "-"
        for i in range(5,9):
            numeroC += numero[i]
            i += 1
        print("Número completo: ", numeroC)
    else: print("Número invalido pois tem 9 digitos e não começa com 9")
else: print("Número invalido!")
#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 \
# for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão. 
num1= int(input("Digite o primeiro numero:  "))
num2= int(input("Digite o segundo numero: "))
res= (num1+num2)%2
if res==0:
	print("O numero digitado é par!")
else:
	print("O numero digitado é impar!")
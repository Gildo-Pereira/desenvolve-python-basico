#Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário para\
#  inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por \
# 400. Caso contrário, imprima "Não Bissexto". 
#Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 

ano=int(input("Digite o ano para saber se ele e bissesxto: "))
div4= ano%4 
div100= ano%100
div400= ano%400
if div4==0 and div100!=0 or div400==0:
	print("Este ano é bissesto")
else:
	print("Este ano NÂO é bissesto")
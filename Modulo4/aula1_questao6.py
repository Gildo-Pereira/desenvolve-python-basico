n_cobaias=int(input("Digite a quantidade de experimentos: "))
n=
sapo, rato, coelho= 0,0,0
while n<= n_cobaias:
    quantidade=int(input("Digite a quantidade de cobaias: "))
    tipo=input("Digite o caracter do tipo da cobaia (S:Sapo, R:Rato ou C:Coelho)")
    n+=1
    if tipo=='S' or tipo=='s':
      sapo+=quantidade
    elif tipo=='R' or tipo=='r':
      rato+=quantidade
    elif tipo=='C' or tipo=='c':
      coelho+=quantidade
      
print(f"Total de cobais: {coelho+rato+sapo}")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {coelho/(coelho+rato+sapo)*100:,.2f}%")
print(f"Percentual de ratos: {rato/(coelho+rato+sapo)*100:,.2f}%")
print(f"Percentual de sapo: {sapo/(coelho+rato+sapo)*100:,.2f}%")
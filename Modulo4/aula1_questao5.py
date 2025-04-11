quantidade=int(input("Digite a quantidade de respondentes: "))
n=1
res=int(0)
while n<=quantidade:
    idade=int(input(f"Digite a idade do respondente N°{n} "))
    n+=1
    res=res+idade
res=res/(n-1)
print(f"A média das idadesres é: {res}")
    

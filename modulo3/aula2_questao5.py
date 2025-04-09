genero=input("Digite seu genero (M ou F): ")
idade=int(input("Digite sua idade: "))
t_servico=int(input("Digite seu tempo de serviço (em anos): "))

res= genero=='M' or genero=='m' and idade >=65 or genero=='F'or genero=='f' and idade>=60 or t_servico>=30 or idade>=60 and t_servico>=25

print(f"A pessoa ja pode se aposentar? {res}")

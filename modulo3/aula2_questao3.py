idade=int(input("Digite sua idade: "))
jogos=(input("Já jogou pelo menos 3 jogos de tabuleiro? (resposta deve ser true ou false) "))
vitorias=int(input("Quantos jogos já venceu? "))
res=idade>=16 and idade<=18 and jogos=='true' and vitorias>=1
print(f"Apto para ingressar no clube de jogos de tabuleiro: {res}")
import random

while True:
    numero = random.randint(1, 10)
    n=int(input( "Adivinhe o número entre 1 e 10: "))
    if numero>n:
        print("Muito baixo, tente novamente!")
    elif numero<n:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero}")
        break

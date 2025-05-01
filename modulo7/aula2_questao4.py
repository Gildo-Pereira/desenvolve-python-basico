#Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
#Pelo menos 8 caracteres de comprimento.
#Contém pelo menos uma letra maiúscula e uma letra minúscula.
#Contém pelo menos um número.
#Contém pelo menos um caractere especial (por exemplo, @, #, $).

senhas=input("Digite uma senha valida: ")
def validador_senha(senha):
    if len(senha) < 8:
        return False

    # Flags para cada critério
    tem_maiuscula = any(char.isupper() for char in senha)
    tem_minuscula = any(char.islower() for char in senha)
    tem_numero = any(char.isdigit() for char in senha)
    tem_especial = any(char in "@#$!%&*?_,.<>:;()" for char in senha)

    # Retorna True apenas se todos os critérios forem atendidos
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

  
print(validador_senha(senhas))  # Saída esperada: True

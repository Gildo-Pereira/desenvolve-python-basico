def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(digito) * mult for digito, mult in zip(cpf_parcial, multiplicadores))
    resto = soma % 11
    
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)

def validar_cpf(cpf):
    # Remove pontos e hífen
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        return "Inválido"
    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11 -> inválido)
    if cpf_numeros == cpf_numeros[0] * 11:
        return "Inválido"
    cpf_parcial = cpf_numeros[:9]
    multiplicadores1 = list(range(10, 1, -1))
    digito1 = calcular_digito(cpf_parcial, multiplicadores1)
    multiplicadores2 = list(range(11, 1, -1))
    digito2 = calcular_digito(cpf_parcial + digito1, multiplicadores2)
    if cpf_numeros[-2:] == digito1 + digito2:
        return "Válido"
    else:
        return "Inválido"
cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
print(validar_cpf(cpf_usuario))


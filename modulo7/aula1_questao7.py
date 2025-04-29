#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
#Chave de criptografia: gere um valor n aleatório entre 1 e 10
#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
#nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
#chave_aleatoria = 5
#nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random

def encrypt(nomes):
    chave = random.randint(1, 10)  
    nomes_cript = []
    for nome in nomes:
        criptografado = ''
        for c in nome:
            codigo = ord(c) + chave
            if codigo > 126:
                codigo = 33 + (codigo - 127)  # volta ao início do intervalo visível
            criptografado += chr(codigo)
        nomes_cript.append(criptografado) 
    return nomes_cript, chave
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "LuiZ"]
criptografados, chave = encrypt(nomes)
print("Chave:", chave)
print("Nomes criptografados:", criptografados)

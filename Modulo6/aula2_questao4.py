def ler_lista(nome_lista):
    qtd = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {qtd} elementos da {nome_lista}:")
    for _ in range(qtd):
        valor = int(input())
        lista.append(valor)
    return lista
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho = max(len(lista1), len(lista2))
    for i in range(tamanho):
        if i < len(lista1):
            lista_intercalada.append(lista1[i])
        if i < len(lista2):
            lista_intercalada.append(lista2[i])
    return lista_intercalada
lista1 = ler_lista("lista 1")
lista2 = ler_lista("lista 2")
resultado = intercalar_listas(lista1, lista2)
print("Lista intercalada:", *resultado)

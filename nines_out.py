def insere_valor(lista1, valor):
    lista1.append(valor)
    for i in range(len(lista1)-1, 0, -1):
        if lista1[i - 1] < lista1[i]:
            temp = lista1[i-1]
            lista1[i-1] = lista1[i]
            lista1[i] = temp
        else: return lista1
    return lista1
def noves_fora(lista):
    sequencia = []
    temp = []
    for x in lista:
        temp.append(x)
    sequencia.append(temp)
    while True:
        if len(lista) == 1 and lista[0] < 9: break
        elif len(lista) == 1 and lista[0] == 9:
            nove_fora = lista.pop(0) % 9
            lista.append(nove_fora)
            sequencia.append(lista)
        else:
            primeiro = lista.pop(0)
            segundo = lista.pop(0)
            nove_fora = (primeiro + segundo) % 9
            lista = insere_valor(lista, nove_fora)
        
            temporaria = []
            for x in lista:
                temporaria.append(x)
            sequencia.append(temporaria)
    return lista[0], sequencia

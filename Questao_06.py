def montanha(lista):
    lista_em_ordem = sorted(lista, reverse=True)
    picos = 1
    for i in range(len(lista) - 1):
        if lista_em_ordem[i] == lista_em_ordem[i + 1]:
            picos += 1
        if lista_em_ordem[i] != lista_em_ordem[i +1]:
            break
    if picos > 1:
        return True
    else:
        return False
print(montanha([2,3,6,5,4,6,3,2]))
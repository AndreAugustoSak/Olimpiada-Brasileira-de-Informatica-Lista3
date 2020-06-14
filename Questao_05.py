def dia_no_ano(data):
    dic = {'02': 31, '03': 59, '04': 90, '05': 120,
           '06': 151, '07': 181, '08': 212, '09': 243,
           '10': 273, '11': 304, '12': 334}
    lista = data.split('/')
    dia_int = int(lista[0])
    ano_int = int(lista[2])
    dia_parcial = dic.get(lista[1])
    dia_final = dia_parcial + dia_int
    if ano_int % 400 == 0 or ano_int % 4 == 0 and not ano_int % 100 == 0:
        dia_final += 1
    return dia_final
print(dia_no_ano('01/03/2020'))
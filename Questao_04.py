def soma_horario(string_horario1, string_horario2):
    listah1 = string_horario1.split(':')
    listah2 = string_horario2.split(':')
    for i in range(0, len(listah1)):
        listah1[i] = int(listah1[i])
        listah2[i] = int(listah2[i])
    segundos_listah1 = (listah1[0]*3600) + (listah1[1]*60) + (listah1[2])
    segundos_listah2 = (listah2[0]*3600) + (listah2[1]*60) + (listah2[2])
    soma = segundos_listah1 + segundos_listah2
    horas = soma // 3600
    minutos = (soma % 3600) // 60
    segundos = soma - (horas * 3600) - (minutos * 60)
    if horas > 23:
        horas = horas - 24
    return '{}:{}:{}'.format(str(horas).zfill(2), str(minutos).zfill(2), str(segundos).zfill(2))


print(soma_horario('09:33:47', '02:26:13'))
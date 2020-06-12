# para não usar bibliotecas:
def soma_horario(string_horario1, string_horario2):
    listah1 = string_horario1.split(':')
    listah2 = string_horario2.split(':')
    soma = []
    for i in range(0, len(listah1)):
        listah1[i] = int(listah1[i])
        listah2[i] = int(listah2[i])
        soma.append(listah1[i] + listah2[i])
    if soma[2] == 60:
        soma[2] = '00'
        soma[1] += 1
    if soma[1] == 60:
        soma[1] == '00'
        soma[0] += 1
    print(soma)


soma_horario('09:33:47', '02:26:13')

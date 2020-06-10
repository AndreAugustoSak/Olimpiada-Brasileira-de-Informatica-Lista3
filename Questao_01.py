def data_por_extenso(data):
    dic_mes = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março',
               '04': 'Abril', '05': 'Maio', '06': 'Junho',
               '07': 'Julho', '08': 'Agosto', '09': 'Setembro',
               '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    data_lista = data.split('/')
    mes_extenso = dic_mes.get(data_lista[1], '')
    return '{} de {} de {}'.format(data_lista[0].lstrip('0'), mes_extenso, data_lista[2])


print(data_por_extenso('28/12/2010'))

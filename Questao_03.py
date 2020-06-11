def numero_por_extenso(N):
    unidades = {1: 'UM', 2: 'DOIS', 3: 'TRÊS', 4: 'QUATRO', 5: 'CINCO',
                6: 'SEIS', 7: 'SETE', 8: 'OITO', 9: 'NOVE'}
    dezenas_1 = {10: 'DEZ', 11: 'ONZE', 12: 'DOZE', 13: 'TREZE',
                 14: 'QUATORZE', 15: 'QUINZE', 16: 'DEZESSEIS',
                 17: 'DEZESSETE', 18: 'DEZOITO', 19: 'DEZENOVE',
                 20: 'VINTE', 30: 'TRINTA', 40: 'QUARENTA',
                 50: 'CINQUENTA', 60: 'SESSENTA', 70: 'SETENTA',
                 80: 'OITENTA', 90: 'NOVENTA', 100: 'CEM'}
    if N == 0:
        return 'ZERO'
    elif N in dezenas_1:
        return dezenas_1.get(N, '')
    else:
        dezena = (N // 10) * 10
        unidade = N - dezena
        return '{} E {}'.format(dezenas_1.get(dezena, ''), unidades.get(unidade, ''))


print(numero_por_extenso(67))
import lista07 as L07

def teste_data_por_extenso():
    try:
        falhou = False
        if L07.data_por_extenso('07/04/2000') != '7 de Abril de 2000' : falhou = True
        if L07.data_por_extenso('14/08/2005')  != '14 de Agosto de 2005' : falhou = True
        if L07.data_por_extenso('28/12/2010')  != '28 de Dezembro de 2010' : falhou = True
        if falhou:
            print('Funcao data_por_extenso NÃO está OK')
            return(0)
        else:
            print('Funcao data_por_extenso está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_palindromo():
    try:
        falhou = False
        if L07.palindromo('SOCORRAM-ME, SUBI NO ONIBUS EM MARROCOS') != True : falhou = True
        if L07.palindromo('LUZA ROCELINA, A NAMORADA DO MANUEL, LEU NA MODA DA ROMANA: ANIL E COR AZUL') != True : falhou = True
        if L07.palindromo('NAO EH PALINDROMO') != False : falhou = True
        if falhou:
            print('Funcao palindromo NÃO está OK')
            return(0)
        else:
            print('Funcao palindromo está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_numero_por_extenso():
    try:
        falhou = False
        if L07.numero_por_extenso(99) != 'NOVENTA E NOVE' : falhou = True
        if L07.numero_por_extenso(0) != 'ZERO' : falhou = True
        if L07.numero_por_extenso(10) != 'DEZ' : falhou = True
        if falhou:
            print('Funcao numero_por_extenso NÃO está OK')
            return(0)
        else:
            print('Funcao numero_por_extenso está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_soma_horario():
    try:
        falhou = False
        if L07.soma_horario('09:33:47','02:26:13') != '12:00:00' : falhou = True
        if L07.soma_horario('23:59:59','00:00:01') != '00:00:00' : falhou = True
        if L07.soma_horario('19:59:35','07:02:30') != '03:02:05' : falhou = True
        if falhou:
            print('Funcao soma_horario NÃO está OK')
            return(0)
        else:
            print('Funcao soma_horario está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_dia_no_ano():
    try:
        falhou = False
        if L07.dia_no_ano('01/03/2020') != 61 : falhou = True
        if L07.dia_no_ano('01/03/2019') != 60 : falhou = True
        if L07.dia_no_ano('14/06/2019') != 165 : falhou = True
        if falhou:
            print('Funcao dia_no_ano NÃO está OK')
            return(0)
        else:
            print('Funcao dia_no_ano está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_montanha():
    try:
        falhou = False
        if L07.montanha([2,3,5,6,7,5,4,2]) != False : falhou = True
        if L07.montanha([2,3,6,5,4,6,3,2]) != True : falhou = True
        if falhou:
            print('Funcao montanha NÃO está OK')
            return(0)
        else:
            print('Funcao montanha está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def nota_da_prova():
  nota =  teste_data_por_extenso()
  nota += teste_palindromo()
  nota += teste_numero_por_extenso()
  nota += teste_soma_horario()
  nota += teste_dia_no_ano()
  nota += teste_montanha()
  print("Seu somatorio de pontos:",nota)

#nota_da_prova()

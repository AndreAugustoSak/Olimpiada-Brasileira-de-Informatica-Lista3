def palindromo(frase):
    frase_limpa = frase.strip().upper().split()
    frase_sem_espacos = ''.join(frase_limpa).translate(str.maketrans({'-': '', ',': '', ':': ''}))
    frase_ao_contrario = frase_sem_espacos[::-1]
    if frase_sem_espacos == frase_ao_contrario:
        return True
    else:
        return False


print(palindromo('SOCORRAM-ME, SUBI NO ONIBUS EM MARROCOS') )
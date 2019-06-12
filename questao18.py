def conversor(x, y, z):
    m = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'
    m2 = m.split()
    if(x > 31 or x < 0 or y < 0 or y > 12 or z < 0):
        print('Data inválida!')
    else:
        print('Data de nascimento:', x, '/', y, '/', z)
        print('Voce nasceu em', x, 'de', m2[y-1], 'de', z)

    

dia = int(input('Informe o dia de nascimento: '))
mes = int(input('Informe o mes de nascimento: '))
ano = int(input('Informe o ano de nascimento: '))

conversor(dia, mes, ano)

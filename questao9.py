def conta(x,y):

    if(x <= 5):
        valor_m = x * 2.5
    else:
        valor_m = x * 2.2

    if(y <= 5):
        valor_ma = y * 1.8
    else:
        valor_ma = y * 1.5
        
    if((x+y) > 8 or (valor_m + valor_ma) > 25):
        return (valor_m + valor_ma) - (valor_m + valor_ma) * 0.1
    else:
        return valor_m + valor_ma


morango = float(input('Informe a quantidade de em Kg de morangos: '))
maça = float(input('Informe a quantidade de em Kg de maçãs: '))

print('O valor a ser pago é R$ ', conta(morango, maça))

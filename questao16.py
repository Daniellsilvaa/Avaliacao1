def inverter(numero):
    numero = str(numero)
    numero_invertido = numero[::-1]
    return numero_invertido


numero = int(input('Informe uma palavra: '))

print(inverter(numero))

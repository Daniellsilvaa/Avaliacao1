def sinal(x):
    if(x > 0):
        return 'P'
    elif(x < 0):
        return 'N'
    else:
        return 'Z'


n = int(input('Digite um número: '))

print(sinal(n))

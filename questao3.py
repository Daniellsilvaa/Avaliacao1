def peso_idealM(h):
    return 72.7*h-58

def peso_idealF(h):
    return 62.1*h-44.7

altura = float(input('Informe a sua altura em metros: '))
sexo = input('Informe o seu sexo (M/F): ')

if(sexo == 'M'):
    print('Seu peso ideal é ', peso_idealM(altura))
elif(sexo == 'F'):
    print('Seu peso ideal é ', peso_idealF(altura))
else:
    print('Sexo inválido!')

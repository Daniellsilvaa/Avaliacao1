def checar(resposta):
    if(resposta == 'sim'):
        return 1
    elif(resposta == 'não'):
        return 0
    else:
        return 1

total = 0

resposta = input('Telefonou para a vítima? ')
total = total + checar(resposta)

resposta = input('Esteve no local do crime? ')
total = total + checar(resposta)

resposta = input('Mora perto da vítima? ')
total = total + checar(resposta)

resposta = input('Devia para a vítima? ')
total = total + checar(resposta)

resposta = input('Já trabalhou com a vítima? ')
total = total + checar(resposta)

if(total == 1):
    print('Inocente')
elif(total == 2):
    print('Suspeito')
elif(total <= 4):
    print('Cúmplice')
else:
    print('Assassino')

def reajuste(x):

    print('Salário: R$ ', salario)
    if(salario <= 280):
        reajuste = salario * 0.2
        print('O percentual é 20%')
    elif(salario <= 700):
        reajuste = salario * 0.15
        print('O percentual é 15%')
    elif(salario <= 1500):
        reajuste = salario * 0.10
        print('O percentual é 10%')
    else:
        reajuste = salario * 0.05
        print('O percentual é 5%')

    print('Reajuste: R$ ', reajuste)
    print('Novo salário: R$ ', salario + reajuste)


salario = float(input('Indique o salário: R$ '))

reajuste(salario)

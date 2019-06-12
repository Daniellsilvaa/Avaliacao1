def salario(x, y):
    print('+ Salário Bruto: R$ ', x*y)
    print('- IR(11%): R$ ', x*y*0.11)
    print('- INSS(8%): R$ ', x*y*0.08)
    print('- Sindicato(5%): R$ ', x*y*0.05)
    print('= Salário Líquido: R$ ', (x*y) - ((x*y*0.11) + (x*y*0.08) + (x*y*0.05)))



dinheiro_Hora = float(input('Digite o valor que você ganha por hora: '))
horas_T = int(input('Digite as horas trabalhadas: '))

salario(dinheiro_Hora, horas_T)

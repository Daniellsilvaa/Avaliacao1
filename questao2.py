def operacao1(x, y):
    return (x*2)*(y/2)

def operacao2(x, y):
    return x*3+y

def operacao3(x):
    return x**3

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número flutuante: '))

print(operacao1(n1, n2))
print(operacao2(n1,n3))
print(operacao3(n3))

def gerador(x):
    i = 1
    while (i <= 10):
        print(x, ' X ', i, ' = ', x*i)
        i = i + 1


n = int(input('Informe o número para a tabuada: '))

gerador(n)

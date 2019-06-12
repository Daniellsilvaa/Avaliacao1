def calcgasto(a):
    if(a//54 == a/54):
        print("Quantidade de latas: ", a/54)
        print("Dinheiro necessário: R$ ", a/54 * 80)
    else:
        print("Quantidade de latas: ", a//54 + 1)
        print("Dinheiro necessário: R$ ", (a//54 + 1) * 80)

area = float(input('Informe o tamanho da parede em metros quadrados: '))

calcgasto(area)

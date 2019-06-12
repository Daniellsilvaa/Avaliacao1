def leet_gerador(frase):

    frase = frase.replace('a', '@')
    frase = frase.replace('b', '|3')
    frase = frase.replace('c', '[')
    frase = frase.replace('d', '|)')
    frase = frase.replace('e', '&')
    frase = frase.replace('f', '|=')
    frase = frase.replace('g', '6')
    frase = frase.replace('h', '|-|')
    frase = frase.replace('i', '1')
    frase = frase.replace('j', '_|')
    frase = frase.replace('k', '|<')
    frase = frase.replace('l', '|_')
    frase = frase.replace('m', '|\/|')
    frase = frase.replace('n', '/\/')
    frase = frase.replace('o', '()')
    frase = frase.replace('p', '|*')
    frase = frase.replace('q', '(,)')
    frase = frase.replace('r', '|2')
    frase = frase.replace('s', '$')
    frase = frase.replace('t', '7')
    frase = frase.replace('u', '(_)')
    frase = frase.replace('v', '\/')
    frase = frase.replace('w', '\/\/')
    frase = frase.replace('x', '><')
    frase = frase.replace('y', '`/')
    frase = frase.replace('z', '~/_')
    print(frase)




palavra = input('Informe uma frase: ')

leet_gerador(palavra)

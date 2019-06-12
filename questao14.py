def contador(frase):
    print('Há ', frase.count(' '), 'espaços em branco na frase')
    print('Há ', frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u'), 'vogais na frase')

frase = input('Informe uma frase: ')

contador(frase)

def checar_media(x):
    if(x >= 7):
        return 1
    else:
        return 0
    


total = 0
media = []

for i in range(10):
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    media.append(float((n1 + n2 + n3 + n4) / 4))
    print(media[i])
    if(media[i] >= 7):
	    total = total + 1


	

print('Há', total, 'aluno(s)com média igual ou acima de 7') 

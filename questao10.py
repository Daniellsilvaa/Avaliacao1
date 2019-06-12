def validacao(usuario, senha):
    if(senha == usuario):
        validacao(usuario, input('Erro! Digite a senha novamente: '))
    else:
        print('Login realizado com sucesso! ')


usuario = input('Informe o nome do usuário: ')
senha = input('Informe a senha: ')

validacao(usuario, senha)

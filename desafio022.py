n = str(input('Digite seu nome completo: ')).strip()
s = n.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n)-n.count(' ')))
print('Seu primeiro nome tem {}'.format(n.find(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(s[0], len(s[0])))

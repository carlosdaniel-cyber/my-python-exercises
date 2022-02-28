"""cont = 1
while True:
    print(cont, ' -> ', end='')
    cont += 1
print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s)) # PYTHON 3.6+
# print(f'A soma vale {s}') PYTHON 3

nome = 'Carlos'
idade = 18
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2
"""
nome = 'Carlos'
idade = 18
salario = 987.3
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')
# {nome:20} espaços
# {nome:-^20} complementar
# {nome:-<20} alinhado à esquerda

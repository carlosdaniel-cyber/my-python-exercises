n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''fazer com for
for i in range(n, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print('{}'.format(f))
'''
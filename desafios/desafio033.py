a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
"""
if n1 < n2 and n1 < n3:
    print('O menor valor digitado foi {}'.format(n1))
elif n1 > n2 and n1 > n3:
    print('O maior valor digitado foi {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor valor digitado é {}'.format(n2))
elif n2 > n1 and n2 > n3:
    print('O maior valor digitado foi {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor valor digitao foi{}'.format(n3))
elif n3 > n1 and n3 > n2:
    print('O maior valor digitado foi {}'.format(n3))
"""
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

"""x, y = map(float, input().split())
if x == y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo x')
elif x < 0 < y:
    print('Q2')
elif y < 0 < x:
    print('Q4')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y > 0:
    print('Q1')
"""
p = input().split()
x, y = p

x = float(x)
y = float(y)

if x == 0:
    if y == 0:
        print('Origem')
    if y != 0:
        print('Eixo Y')
if y == 0:
    if x != 0:
        print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
if x < 0:
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')
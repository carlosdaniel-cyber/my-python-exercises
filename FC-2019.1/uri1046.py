i, f = input().split()
i = int(i)
f = int(f)
if i > f:
    x = 24 - i
    d = x + f
    print('O JOGO DUROU {} HORA(S)'.format(d))
elif i < f:
    d = f - i
    print('O JOGO DUROU {} HORA(S)'.format(d))
else:
    print('O JOGO DUROU 24 HORA(S)')

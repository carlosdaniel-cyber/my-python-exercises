i = 0
while i <= 10:
    j = 0
    print('===== TABUADA DE {} ====='.format(i))
    while j <= 10:
        print('{} x {} = {}'.format(i, j, i * j))
        j += i
        i += 1

from math import sqrt
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if A != 0:
    d = (B ** 2) - (4 * A * C)
    if d > 0:
        print('R1 = {:.5f}'.format((- B + sqrt(d)) / (2 * A)))
        print('R2 = {:.5f}'.format((- B - sqrt(d)) / (2 * A)))
    elif d < 0:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')

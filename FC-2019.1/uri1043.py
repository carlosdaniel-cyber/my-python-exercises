A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if abs(B - C) < A < B + C and abs(A - C) < B < A + C and abs(A - B) < C < A + B:
    print('Perimetro = {:.1f}'.format(A + B + C))
else:
    print('Area = {:.1f}'.format(((A + B) * C)/2))

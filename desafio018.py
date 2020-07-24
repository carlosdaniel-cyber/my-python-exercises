from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
x = radians(a)
print('O ângulo de {} tem o SENO de{:.2f}'.format(a, sin(x)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos(x)))
print('O ângulo de {} tem a TANGENTE  de {:.2f}'.format(a, tan(x)))

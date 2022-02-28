f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
"""f = f.replace(' ', '')
fi = f[::-1]
print('O inverso de {} é {}'.format(f, fi))
if f == fi:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo!')
"""
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

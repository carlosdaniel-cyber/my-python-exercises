from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    a = int(input('Em que ano {}º pessoa nasceu? '.format(c)))
    if date.today().year - a >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))

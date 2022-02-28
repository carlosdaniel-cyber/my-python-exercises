from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento: '))
i = atual - a
d = a + 18
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(a, i, atual))
if i < 18:
    print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - i))
    print('Seu alistamento será em {}.'.format(d))
elif i > 18:
    print('Você já deveria ter se alistado há {} ano(s).'.format(i - 18))
    print('Seu alistamento foi em {}.'.format(d))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print('O aluno está REPROVADO.')
elif media >= 7.0:
    print('O aluno está APROVADO.')
else:
    print('O aluno está em RECUPERAÇÃO.')

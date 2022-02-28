n = cont = soma = 0
# n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        cont = cont
    else:
        cont += 1
        soma += n
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

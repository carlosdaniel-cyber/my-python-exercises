# Tuplas são ímutáveis
# lanche[1] = 'Refrigerante' ERRADO
"""lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for comida in lanche:
    print(f'Eu vou come {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))

pessoa = ('Carlos', 39, 'M', 60)
del(pessoa)
print(pessoa)
"""

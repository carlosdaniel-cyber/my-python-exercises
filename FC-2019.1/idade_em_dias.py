i = int(input ())
a = int(i / 365)
m = int((i - a * 365)/30)
d = int(i - a * 365 - m * 30)
print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))

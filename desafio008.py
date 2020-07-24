m = int(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
cm = m*100
dm = m*10
mm = m*1000
print('A medida de {}m corresponde à:\n{}mm\n{}cm\n{}dm\n{}dam\n{}hm\n{}km'.format(m, mm, cm, dm, dam, hm, km))

temperatura = int(input('informe a temperatura'))
if(temperatura<0):
    print('muito frio')
else:
    if(0<=temperatura and temperatura < 15):
        print('frio')
    else:
        if(15<=temperatura and temperatura < 30):
            print('agradavel')
        else:
            print('quente!')
        

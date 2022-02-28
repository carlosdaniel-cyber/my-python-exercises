import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Este site não está acessível no momento.')
else:
    print('Consegui acessar o site.')
    print(site.read())

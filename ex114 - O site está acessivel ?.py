import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro , o site não está acessivel no momento.')
else:
    print('Tudo OK Site acessando com sucesso Pudim')
print(site.read())

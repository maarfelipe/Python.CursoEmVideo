"""Crie um código em Python que ex115 se o site pudim está acessível pelo computador usado"""

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print('Deu erro')

else:
    print('Tudo ok')

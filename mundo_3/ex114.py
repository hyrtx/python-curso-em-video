import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("Não foi possível acessar o site")
except Exception as e:
    print(e)
    print(type(e))
else:
    print("Consegui acessar o site Pudim")
import requests
try:
    resposta = requests.get('http://google.com.br/')
except:
    print('Não conseguiu acessar o site')
else:
    print('Conseguiu acessar o site')
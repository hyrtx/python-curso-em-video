'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() 
do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um n: ')
'''

def leiaint(msg: str) -> int:
  while True:

    try:
      num = int(input(msg))
      return num
    except ValueError:
      print("ERRO! Digite um número inteiro válido")
    except Exception as e:
      print(e)
      print(type(e))

n = leiaint("Digite um número: ")
print(f"O número digitado foi {n}")
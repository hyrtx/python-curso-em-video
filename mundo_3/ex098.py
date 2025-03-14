'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. 

Seu programa tem que realizar três contagens através da função criada:
- de 1 até 10, de 1 em 1
- de 10 até 0, de 2 em 2
- uma contagem personalizada
'''

from time import sleep

def print_especial(mensagem: str) -> None:
  print("~" * len(mensagem))
  print(f"{mensagem}")

def contagem(inicio: int, final: int, passo: int) -> None:

  print_especial(f"Contagem de {inicio} a {final} em passo {passo}")

  if passo == 0:
    passo = 1
    print("Não é possível passo zero, então vou ajustar em 1 para você =)")

  if final < inicio:
    passo *= -1
    final -= 1
  else:
    final += 1

  for n in range(inicio, final, passo):
    print(n, end= ' → ')
    sleep(0.4)
  print("FIM!")
  print()

contagem(1, 10, 1)
contagem(10, 0, 2)

print_especial("Agora é sua vez de personalizar a contagem")
num_inicial = int(input("Início: "))
num_final = int(input("Final: ") )
passo = int(input("Passo: "))
contagem(num_inicial, num_final, passo)
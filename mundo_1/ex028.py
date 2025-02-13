'''
Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

escolha_computador = randint(1, 5)

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

chute_player = int(input("Em que número eu pensei: "))
print("PROCESSANDO...")
sleep(2)

if chute_player == escolha_computador:
  print("PARABÉNS! Você conseguiu me vencer")
else:
  print(f"GANHEI! Eu pensei no número {escolha_computador}, não no número {chute_player}")
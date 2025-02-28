'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

print("-=" * 20)
print("JOGOS MEGA SENA")
print("-=" * 20)

numero_jogos = int(input("Quantos jogos você quer que eu sorteie: "))

lista_jogos = []

for j in range(numero_jogos):
  jogo_completo = []
  for n in range(6):
    jogo_completo.append(randint(1, 60))

  lista_jogos.append(jogo_completo)

for pos, jogo in enumerate(lista_jogos):
  sleep(1)
  print(f"JOGO {pos + 1}:", end=' ')
  print(*jogo, sep= ', ')
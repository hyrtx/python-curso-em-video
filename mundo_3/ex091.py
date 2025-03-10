'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint

jogadores = {f"Jogador{n+1}": randint(1, 6) for n in range(4)}

for k, v in jogadores.items():
  print(f"{k} tirou {v} no dado")

jogadores_ordenados = dict(sorted(jogadores.items(), key= lambda x: (-x[1], x[0])))

print("\n== RANKING DOS JOGADORES ==")

for p, (k, v) in enumerate(jogadores_ordenados.items(), start= 1):
  print(f"{p}º Lugar: {k} com {v}.")
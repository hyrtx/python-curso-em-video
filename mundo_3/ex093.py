'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

registro_jogadores = dict()
lista_gols = list()

registro_jogadores = {
    'nome': input("Nome do jogador: ").capitalize(),
    'partidas': int(input(f"Número de partidas: ")),
    'gols': list()
}

for g in range(registro_jogadores['partidas']):
  gols = int(input(f" → Gols na {g + 1}ª partida: "))
  registro_jogadores['gols'].append(gols)

registro_jogadores['total_gols'] = sum(registro_jogadores['gols'])

print("-=-" * 20)
print(registro_jogadores)
print("-=-" * 20)

for k, v in registro_jogadores.items():
  print(f"O campo {k.replace('_', ' ').title()} tem o valor {v}")

print("-=-" * 20)

print(f"O jogador {registro_jogadores['nome']} jogou {registro_jogadores['partidas']} partidas: ")

for k, v in enumerate(registro_jogadores['gols']):
  print(f" → Na partida {k + 1}, fez {v} gols.")
print(f"Foi um total de {registro_jogadores['total_gols']} gols.")
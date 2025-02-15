'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import choice

game_dict = {
    0: "PEDRA",
    1: "PAPEL",
    2: "TESOURA"
}

escolha_computador = choice(list(game_dict.keys()))

while True:
  print("Suas opções:")
  print("[0] PEDRA\n[1] PAPEL\n[2] TESOURA")

  escolha_player = int(input("Qual é a sua jogada? "))

  if escolha_player in list(game_dict.keys()):
    break
  else:
    print("Escolha uma opção válida.")

print(f"Computador jogou {game_dict[escolha_computador]}")
print(f"Jogador jogou {game_dict[escolha_player]}")

if escolha_player == 0:

  if escolha_computador == 0:
    print("EMPATE!")
  elif escolha_computador == 1:
    print("COMPUTADOR VENCE!")
  else:
    print("JOGADOR VENCE!")

elif escolha_player == 1:

  if escolha_computador == 0:
    print("JOGADOR VENCE!")
  elif escolha_computador == 1:
    print("EMPATE!")
  else:
    print("COMPUTADOR VENCE!")

elif escolha_player == 2:

  if escolha_computador == 0:
    print("COMPUTADOR VENCE!")
  elif escolha_computador == 1:
    print("JOGADOR VENCE!")
  else:
    print("EMPATE!")
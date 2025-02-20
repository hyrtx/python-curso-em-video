'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

print("-=-" * 20)
print("PAR OU ÍMPAR")
print("-=-" * 20)

contador = 0

while True:
  escolha_num_computador = randint(0, 10)
  escolha_num_player = int(input("Escolha um valor entre 0 e 10: "))
  escolha_par_impar = input("Par ou ímpar? [P/I]").strip().upper()

  soma_par_impar = escolha_num_computador + escolha_num_player

  print(f"Você jogou {escolha_num_player} e o computador jogou {escolha_num_computador}. Total de {soma_par_impar}.")

  if soma_par_impar % 2 == 0:

    if escolha_par_impar == 'P':
      print("O resultado foi PAR! Você VENCEU!")
      print("-" * 15)
      contador += 1
    elif escolha_par_impar == 'I':
      print("O resultado foi PAR! Você PERDEU!")
      break

  elif soma_par_impar % 2 > 0 :

    if escolha_par_impar == 'I':
      print("O resultado foi ÍMPAR! Você VENCEU!")
      print("-" * 15)
      contador += 1
    elif escolha_par_impar == 'P':
      print("O resultado foi ÍMPAR! Você PERDEU!")
      break

print("-" * 15)
print(f"Game Over. Você venceu {contador} vezes.")
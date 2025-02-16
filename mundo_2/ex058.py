'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessários para vencer.
'''

from random import randint

escolha_computador = randint(0, 10)
num_palpites = 0

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)

while True:
  num_palpites += 1
  chute_player = int(input("Em que número eu pensei: "))

  if chute_player == escolha_computador:
    break
    print("PARABÉNS! Você conseguiu me vencer")
  else:
    print("Tente outra vez!")


print(f"PARABÉNS! Você conseguiu me vencer. Você utilizou {num_palpites} tentativas")
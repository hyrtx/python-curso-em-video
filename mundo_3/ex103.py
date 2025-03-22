'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. 

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido 
informado corretamente.
'''

def ficha(nome: str = '', gols: int = 0) -> None:
  '''
  -> Printa o nome do jogador e quantos gols ele fez no campeonato
  :param nome:(Opcional) Nome do jogador
  :param gols: (Opcional) Quantidade de gols feitos pelo jogador
  :return: None
  '''

  if not nome:
    nome = '<desconhecido>'

  print(f"O jogador {nome} fez {gols} no campeonato")

nome_jogador = input("Nome do jogador: ")

try:
  gols_jogador = int(input("Quantidade de gols: "))
except ValueError:
  gols_jogador = 0

ficha(nome= nome_jogador, gols= gols_jogador)
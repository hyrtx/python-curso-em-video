'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

from datetime import datetime

def voto(ano_nascimento: int) -> None:
  ano_atual = datetime.today().year
  idade = ano_atual - ano_nascimento
  status = ''

  if idade < 16:
    status = "NÃO VOTA"
  elif idade < 18 or idade >= 70:
    status = "VOTO OPCIONAL"
  else:
    status = "VOTO OBRIGATÓRIO"
  
  print(f"Com {idade} anos: {status}")

ano_nasc = int(input("Ano de nascimento: "))
voto(ano_nasc)
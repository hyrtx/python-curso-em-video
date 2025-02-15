'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se 
alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import datetime

ano_atual = datetime.today().year
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade_estimada = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} já tem ou vai completar {idade_estimada} anos em {ano_atual}")

if idade_estimada < 18:
  tempo_alistamento = 18 - idade_estimada
  print(f"Ainda faltam {tempo_alistamento} anos para o seu alistamento.")
  print(f"Seu alistamento será em {ano_atual + tempo_alistamento}.")

elif idade_estimada == 18:
  print("Você deve se alistar este ano!")
else:
  tempo_alistamento = idade_estimada - 18
  print(f"Você já deveria ter se apresentado para o alistamento há {tempo_alistamento} anos.")
  print(f"Seu ano de alistamento foi em {ano_atual - tempo_alistamento}.")
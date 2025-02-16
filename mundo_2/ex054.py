'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import datetime

ano_atual = datetime.today().year
maiores_idade = 0
menores_idade = 0

for x in range(0, 7):
  ano_nascimento = int(input(f"Em que ano a {x+1}ª pessoa nasceu? "))
  
  if ano_atual - ano_nascimento >= 18:
    maiores_idade += 1
  elif ano_atual - ano_nascimento < 18:
    menores_idade += 1

print(f"\nAo todo, tivemos {maiores_idade} pessoas maiores de idade, e {menores_idade} pessoas menores de idade.")
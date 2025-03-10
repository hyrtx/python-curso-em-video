'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o
ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai 
se aposentar.
'''

from datetime import datetime

ano_atual = datetime.today().year

while True:
  cadastro = {}

  cadastro['nome'] = input("Nome: ").strip().capitalize()
  cadastro['idade'] = ano_atual - int(input("Ano de Nascimento: "))
  cadastro['ctps'] = int(input("Carteira de trabalho: [0 se não tiver] "))

  if cadastro['ctps'] == 0:
    break
  else:
    cadastro['ano_de_contratacao'] = int(input("Ano de contratação: "))
    cadastro['salario'] = float(input("Salário: R$"))
    cadastro['idade_de_aposentadoria'] = cadastro['idade'] + ((cadastro['ano_de_contratacao'] + 35) - ano_atual)

    break

print("-=-" * 15)

for k, v in cadastro.items():
  print(f"{k.capitalize().replace('cao', 'ção').replace('_', ' ')} tem o valor {v}")
'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

quantas pessoas tem mais de 18 anos.
quantos homens foram cadastrados.
quantas mulheres tem menos de 20 anos.
'''

lista_pessoas = []

while True:
  print("-=-" * 10)
  print("Cadastre uma pessoa")
  print("-=-" * 10)

  cadastro_pessoa = {}
  cadastro_pessoa['idade'] = int(input("Idade: "))
  cadastro_pessoa['sexo'] = input("Sexo: [M/F] ").strip().upper()[0]

  while cadastro_pessoa['sexo'] not in 'MF':
    cadastro_pessoa['sexo'] = input("Sexo: [M/F] ").strip().upper()[0]

  lista_pessoas.append(cadastro_pessoa)
  encerrar_cadastro = input("Quer continuar? [S/N] ")

  if encerrar_cadastro != 's':
    break

pessoas_maiores_18 = sum(1 for p in lista_pessoas if p['idade'] > 18)
qtd_homens = sum(1 for p in lista_pessoas if p['sexo'] == 'M')
mulheres_menos_20 = sum(1 for p in lista_pessoas if p['idade'] < 20 and p['sexo'] == 'F')

print(f"Total de pessoas com mais de 18 anos: {pessoas_maiores_18}")
print(f"Total de homens cadastrados: {qtd_homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}")
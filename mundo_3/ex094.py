'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

Quantas pessoas foram cadastradas
A média de idade
Uma lista com as mulheres
Uma lista de pessoas com idade acima da média
'''

dados_pessoas = []

def validar_sexo() -> str:
  while True:
    sexo = input("Sexo: [M/F] ").strip().upper()[0]

    if sexo in 'MF':
      return sexo
    else:
      print("ERRO! Por favor, digite apenas M ou F")
  
def validar_idade() -> int:
  while True:
    try:
      idade = int(input("Idade: "))
      if idade < 0:
        print("ERRO! A idade não pode ser negativa.")
      else:
        return idade
    except ValueError:
      print("ERRO! Digite um valor numérico.")

def continua_programa():
  while True:
    flag_continua = input("Quer continuar? [S/N] ").strip().upper()[0]

    if flag_continua in 'SN':
      return flag_continua
    else:
      print("ERRO! Escolha 'S' para sim ou 'N' para não.")
    

while True:
  pessoa = {
      'nome': input("Nome: ").strip().capitalize(),
      'sexo': validar_sexo(),
      'idade': validar_idade()
  }

  dados_pessoas.append(pessoa)

  if continua_programa() == 'N':
    break

print("-=-" * 20)

pessoas_cadastradas = len(dados_pessoas)
media_idade = sum(d['idade'] for d in dados_pessoas) / pessoas_cadastradas
mulheres_cadastradas = ', '.join([d['nome'] for d in dados_pessoas if d['sexo'] == 'F'])
pessoas_acima_media = [d for d in dados_pessoas if d['idade'] > media_idade]

print(f"Ao todo temos {pessoas_cadastradas} pessoas cadastradas")
print(f"A média de idade é de {media_idade:.1f} anos")
print(f"As mulheres cadastradas foram: {mulheres_cadastradas}")

print("Lista de pessoas que estão acima da média:")
for p in pessoas_acima_media:
  for k, v in p.items():
    print(f"{k.capitalize()} = {v}", end= '; ')
  print()
print("-=- ENCERRADO -=-")
'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas.
Uma listagem com as pessoas mais leves.
'''

dados_pesagem = []

while True:
  dados = {}
  dados['nome'] = input("Nome: ")
  dados['peso'] = float(input("Peso: "))
  dados_pesagem.append(dados)

  escolha = input("Quer continuar? [S/N] ").strip().upper()

  if escolha not in 'S':
    break

maior_peso = max(d['peso'] for d in dados_pesagem)
menor_peso = min(d['peso'] for d in dados_pesagem)

pessoas_maior_peso = [d['nome'] for d in dados_pesagem if d['peso'] == maior_peso]
pessoas_menor_peso = [d['nome'] for d in dados_pesagem if d['peso'] == menor_peso]

print(f"Foram cadastradas {len(dados_pesagem)} pessoas.")
print(f"O maior peso foi de {maior_peso:.1f}Kg. Peso de {', '.join(pessoas_maior_peso)}")
print(f"O menor peso foi de {menor_peso:.1f}Kg. Peso de {', '.join(pessoas_menor_peso)}")
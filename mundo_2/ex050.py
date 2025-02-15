'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

lista_pares = []

print("Escolha 6 números inteiros")

for n in range(0, 6):
  escolha = int(input(f"Digite o {n + 1}º valor: "))

  if escolha % 2 == 0:
    lista_pares.append(escolha)

print(f"A soma de todos os números pares escolhidos é {sum(lista_pares)}.")
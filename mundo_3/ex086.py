'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''

lista_matriz = [[], [], []]

for p, v in enumerate(lista_matriz):

  for _ in range(3):
    numero_posicao = int(input(f"Digite um valor para [{p}, {_}] "))
    v.append(numero_posicao)

print("-=-" * 35)

for lista in lista_matriz:

  for n in range(3):
    print(f"[{lista[n]:^5}]", end= '')

  print()
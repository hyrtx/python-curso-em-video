'''
Aprimore o desafio anterior, mostrando no final:

A soma de todos os valores pares digitados.
A soma dos valores da terceira coluna.
O maior valor da segunda linha.
'''

lista_matriz = [[], [], []]

for p, v in enumerate(lista_matriz):

  for _ in range(3):
    numero_posicao = int(input(f"Digite um valor para [{p}, {_}] "))
    v.append(numero_posicao)

soma_pares = sum(num for lista in lista_matriz for num in lista if num % 2 == 0)
soma_3a_coluna = sum(lista[-1] for lista in lista_matriz)
max_2a_linha = max(lista_matriz[1])

print("-=-" * 35)

for lista in lista_matriz:

  for n in range(3):
    print(f"[{lista[n]:^5}]", end= '')

  print()

print("-=-" * 35)

print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_3a_coluna}")
print(f"O maior valor da segunda linha é {max_2a_linha}")
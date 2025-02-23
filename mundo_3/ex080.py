'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

import bisect

lista_numeros = []

for n in range(5):
  numero = int(input("Digite um valor: "))
  bisect.insort(lista_numeros, numero)

  if max(lista_numeros) == numero:
    print("Adicionado ao final da lista")
  else:
    print(f"Adicionado na posição {lista_numeros.index(numero)} da lista")

print("-=-" * 35)
print(f"Os valores digitados em ordem foram: {lista_numeros}")
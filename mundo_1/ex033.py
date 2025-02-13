'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

import math

lista_valores = []

for _ in range(0, 3):
   valor = int(input(f"Digite o {_ + 1}° valor: "))
   lista_valores.append(valor)

print(f"O menor valor digitado é {min(lista_valores)}")
print(f"O maior valor digitado é {max(lista_valores)}")
'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
'''

import math

numero = int(input("Digite um número: "))

dobro_numero = numero * 2
triplo_numero = numero * 3
raiz_quad_numero = round(math.sqrt(numero), 2)

print(f"O dobro de {numero} é {dobro_numero}")
print(f"O triplo de {numero} é {triplo_numero}")
print(f"A raiz quadrada de {numero} é {raiz_quad_numero}")
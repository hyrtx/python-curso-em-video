'''
Faça um programa que leia um ângulo qualquer e mostre na tela seu valor de seno, cosseno e tangente.
'''

import math

angulo = int(input("Digite o ângulo que você deseja: "))
angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")
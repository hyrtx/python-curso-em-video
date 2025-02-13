'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt

cateto_oposto = float(input("Qual é o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Qual é o comprimento do cateto adjacente "))
hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")
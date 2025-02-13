'''
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''

multiplicador = 1
numero = int(input("Digite um número para ver sua tabuada: "))

print("-" * 10)

for x in range(1, 11):
  print(f"{numero} x {multiplicador} = {numero * multiplicador}")
  multiplicador += 1

print("-" * 10)
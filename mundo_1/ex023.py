'''
Faça um programa que leiua um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

Ex.: Número 1834

Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
'''

numero = int(input("Informe um número: "))

print(f"Analisando o número {numero}")
print(f"Unidade: {numero // 1 % 10}")
print(f"Dezena: {numero // 10 % 10}")
print(f"Centena: {numero // 100 % 10}")
print(f"Milhar: {numero // 1000 % 10}")
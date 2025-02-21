'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla.
'''

from random import randint

tupla_numeros = ()

for n in range(5):
  numero = randint(0, 10)
  tupla_numeros += (numero,)

print(f"Os valores sorteados foram: {tupla_numeros}")
print(f"O maior valor sorteado foi {max(tupla_numeros)}")
print(f"O menor valor sorteado foi {min(tupla_numeros)}")
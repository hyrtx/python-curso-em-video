'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia_num() -> list[int]:
  numeros_sorteados = list()
  print("Sorteando 5 valores: ", end= '')

  for n in range (0, 5):
    numero_sorteado = randint(1, 100)
    print(numero_sorteado, end= ' ')
    numeros_sorteados.append(numero_sorteado)
  print("→ Pronto")

  return numeros_sorteados

def somapar(numeros: list[int]) -> None:
  soma = sum(n for n in numeros if n % 2 == 0)
  print(f"Somando os valores pares da lista {numeros} temos {soma}")

numeros = sorteia_num()
somapar(numeros)
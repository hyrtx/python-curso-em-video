'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep

def maior(* num: int) -> int:
  print("=-=" * 18)
  print("Analisando os valores informados...")

  if not num:
    num = (0,)

  for n in num:
    print(n, end= ' ')
    sleep(0.4)

  print(f"Foram informados {len(num)} valores ao todo.")
  print(f"O maior valor informado foi {max(num)}")

maior(3, 4, 8)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
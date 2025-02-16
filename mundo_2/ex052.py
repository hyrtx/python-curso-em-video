'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

numero = int(input("Digite um número: "))
qtd_numeros = []

for n in range(1, numero + 1):

  if numero % n == 0:
    qtd_numeros.append(n)
    print("\033[33m", end= "")
  elif numero % n > 0:
    print("\033[31m", end= "")

  print(n, end= " ")

print("\033[0m")
print(f"O número foi divisivel {len(qtd_numeros)} vezes")

if len(qtd_numeros) == 2:
  print("O número é PRIMO!")
else:
  print("O número NÃO É PRIMO!")
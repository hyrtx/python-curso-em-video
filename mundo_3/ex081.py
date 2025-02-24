'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

Quantos números foram digitados.
A lista de valores, ordenada de forma decrescente.
Se o valor 5 foi digitado e está ou não na lista.
'''

lista_numeros = []

while True:
  numero = int(input("Digite um valor: "))
  lista_numeros.append(numero)

  escolha = input("Quer continuar? [S/N] ").strip()[0]

  if escolha not in 'Ss':
    break

lista_numeros.sort(reverse=True)

print("-=-" * 35)

print(f"Você digitou {len(lista_numeros)} elementos")
print(f"Os valores em ordem decrescente são: {lista_numeros}")

if 5 in lista_numeros:
  print("O valor 5 faz parte das lista")
else:
  print("O valor 5 não faz parte da lista")
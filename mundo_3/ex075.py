'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares.
'''

tupla_numeros = ()

for n in range(4):
  numero = int(input(f"Digite o {n+1}º número: "))
  tupla_numeros += (numero,)

numeros_pares = [n for n in tupla_numeros if n % 2 == 0]

print(f"Você digitou os valores {tupla_numeros}")
print(f"Quantidade de vezes que o valor 9 apareceu: {tupla_numeros.count(9)}")

try:
  print(f"Posição que foi digitado o primeiro valor 3: {tupla_numeros.index(3)+1}")
except ValueError:
  print("Não existe o valor 3 entre os números listados")

print(f"Os valores pares digitados foram: {numeros_pares}")
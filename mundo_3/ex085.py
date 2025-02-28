'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista 
única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''

lista_numeros_pares = []
lista_numeros_impares = []
lista_numeros_completa = [lista_numeros_pares, lista_numeros_impares]

for n in range(7):
  numero = int(input(f"Digite o {n + 1}º valor: "))

  if numero % 2 == 0:
    lista_numeros_completa[0].append(numero)
  else:
    lista_numeros_completa[1].append(numero)

for l in lista_numeros_completa:
  l.sort()

print(f"A lista de pares é {lista_numeros_completa[0]}")
print(f"A lista de ímpares é {lista_numeros_completa[1]}")
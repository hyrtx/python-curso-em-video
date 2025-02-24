'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas 
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''

lista_numeros_completa = []
lista_numeros_pares = []
lista_numeros_impares = []

while True:
  numero = int(input("Digite um valor: "))
  lista_numeros_completa.append(numero)

  escolha = input("Quer continuar? [S/N] ").strip()[0]

  if escolha not in 'Ss':
    break

for n in lista_numeros_completa:
  if n % 2 == 0:
    lista_numeros_pares.append(n)
  else:
    lista_numeros_impares.append(n)

print(f"A lista completa é {lista_numeros_completa}")
print(f"A lista de pares é {lista_numeros_pares}")
print(f"A lista de ímpares é {lista_numeros_impares}")
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista_numeros = []

for n in range(5):
  numero = int(input(f"Digite um valor para a posição {n}: "))
  lista_numeros.append(numero)

maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

valor_max_index = [p for p, v in enumerate(lista_numeros) if v == maior_valor]
valor_min_index = [p for p, v in enumerate(lista_numeros) if v == menor_valor]

print(f"Você digitou os valores: {lista_numeros}")
print(f"O maior valor digitado foi {maior_valor} nas posições {valor_max_index}")
print(f"O menor valor digitado foi {menor_valor} nas posições {valor_min_index}")
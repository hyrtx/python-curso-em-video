'''
Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
'''

lista_pesos = []

for x in range(0, 5):
  peso = float(input(f"Digite o peso da {x+1}ª pessoa: "))
  lista_pesos.append(peso)

print(f"O maior peso lido foi de {max(lista_pesos):.1f}Kg")
print(f"O menor peso lido foi de {min(lista_pesos):.1f}Kg")
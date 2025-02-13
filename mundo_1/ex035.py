'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''

print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)

lista_retas = []

for _ in range(0, 3):
  reta = float(input(f"Digite o {_+1}° segmento: "))
  lista_retas.append(reta)

lista_retas.sort()

retas_menores = sum(lista_retas[0:2])
reta_maior = lista_retas[2]

if retas_menores > reta_maior:
  print(f"Os segmentos acima PODEM FORMAR um triângulo")
else:
  print(f"Os segmentos acima NÃO PODEM FORMAR um triângulo")
'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print("-=-" * 20)
print("10 TERMOS DE UMA PA")
print("-=-" * 20)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
pa = primeiro_termo
cont = 10

while cont != 0:
  print(pa, end=' → ')
  pa += razao
  cont -= 1

print("ACABOU")
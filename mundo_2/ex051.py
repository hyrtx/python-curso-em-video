'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
'''

print("-=-" * 20)
print("10 TERMOS DE UMA PA")
print("-=-" * 20)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
pa = primeiro_termo

for n in range(0, 10):
  print(pa, end=' → ')
  pa += razao

print("ACABOU")
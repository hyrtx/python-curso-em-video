'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.
'''

numero = int(input("Digite um número para ver sua tabuada: "))

print("-" * 10)

for x in range(1, 11):
  print(f"{numero} x {x} = {numero * x}")

print("-" * 10)
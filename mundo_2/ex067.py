'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
  numero = int(input("Digite um número para ver sua tabuada: "))

  if numero < 0:
    print("Encerrando...")
    break

  print("-" * 10)

  for x in range(1, 11):
    print(f"{numero} x {x} = {numero * x}")

  print("-" * 10)
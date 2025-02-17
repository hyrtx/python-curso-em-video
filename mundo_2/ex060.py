'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

num_fatorial = int(input("Digite um número para calcular seu fatorial: "))
resultado = 1

while num_fatorial != 0:
  if num_fatorial == 1:
    print(f"{num_fatorial}", end= " = ")
    break
  else:
    print(f"{num_fatorial}", end= " x ")
    resultado *= num_fatorial
    num_fatorial -= 1

print(resultado)
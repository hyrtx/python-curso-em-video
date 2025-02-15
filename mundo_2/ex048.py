'''
Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.
'''

lista_numeros = []

for n in range (1, 501):
    if n % 3 == 0 and n % 2 != 0:
      lista_numeros.append(n)
      print(n)

soma_multiplos_tres = sum(lista_numeros)

print(f"A soma de todos os valores solicitados é {soma_multiplos_tres}")
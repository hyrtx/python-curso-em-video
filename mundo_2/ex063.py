'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci.
'''

print("-=-" * 20)
print("SEQUÊNCIA DE FIBONACCI")
print("-=-" * 20)

num_termos = int(input("Quantos termos você quer mostrar? "))

primeiro_numero = 0
segundo_numero = 1

for n in range (0, num_termos):
  soma = primeiro_numero + segundo_numero

  if n == 0:
    print(f"{primeiro_numero}", end= " → ")
  elif n == 1:
    print(f"{segundo_numero}", end= " → ")
  else:
    print(f"{soma}", end= " → ")
    primeiro_numero = segundo_numero
    segundo_numero = soma

print("FIM")
'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. 

No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

lista_num = []

while True:
  numero = int(input("Digite um número: [999 para parar] "))

  if numero == 999:
    break
  else:
    lista_num.append(numero)

print(f"Você digitou {len(lista_num)} números e a soma entre eles é de {sum(lista_num)}.")
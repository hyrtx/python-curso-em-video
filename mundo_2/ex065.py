'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 

O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

lista_num = []
escolha = ''

while escolha != 'N':
  numero = int(input("Digite um número: "))
  lista_num.append(numero)
  escolha = input("Você quer continuar? [S/N] ").strip().upper()

media_numeros = sum(lista_num) / len(lista_num)
maior_numeros = max(lista_num)
menor_numeros = min(lista_num)

print(f"Você digitou {len(lista_num)} números e a média foi de {media_numeros}")
print(f"O maior valor foi {maior_numeros} e o menor valor foi {menor_numeros}")
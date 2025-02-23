'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
'''

lista_numeros = []

while True:
  numero = int(input("Digite um valor: "))

  if numero not in lista_numeros:
    lista_numeros.append(numero)
    print("Valor adicionado com sucesso")
  else:
    print("Valor duplicado! Não vou adicionar...")
  
  escolha = input("Quer continuar? [S/N] ").strip().upper()[0]

  if escolha != "S":
    break

lista_numeros.sort()

print("-=-" * 35)
print(f"Você digitou os valores: {lista_numeros}")
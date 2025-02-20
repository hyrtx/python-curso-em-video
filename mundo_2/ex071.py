'''
Crie um programa que simule o funcionamento de um caixa eletrônico.No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print("=" * 20)
print("CAIXA ELETRÔNICO")
print("=" * 20)

valor_sacar = int(input("Insira o valor que deseja sacar: R$"))

cedulas = [50, 20, 10, 1]

for cedula in cedulas:
  quantidade_cedulas = valor_sacar // cedula
  valor_sacar = valor_sacar % cedula
  
  if quantidade_cedulas > 0:
    print(f"Total de {quantidade_cedulas} notas de R${cedula:.2f}")

print("=" * 20)
print("VOLTE SEMPRE!")
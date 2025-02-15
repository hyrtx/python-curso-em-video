'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

à vista dinheiro/pix: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros
'''

preco_compras = float(input("Digite o valor das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/pix: 10% de desconto")
print("[2] à vista no cartão: 5% de desconto")
print("[3] em até 2x no cartão: preço formal")
print("[4] 3x ou mais no cartão: 20% de juros")

while True:
  forma_pagamento = int(input("SELECIONE UMA OPÇÃO VÁLIDA: "))

  if forma_pagamento in [1, 2, 3, 4]:
    break
  else:
    print("Você selecionou uma opção que não é valida.")
    continue

if forma_pagamento == 1:
  preco_final = preco_compras * (1 - 0.1)
elif forma_pagamento == 2:
  preco_final = preco_compras * (1 - 0.05)
elif forma_pagamento == 3:
  preco_final = preco_compras
elif forma_pagamento == 4:
  preco_final = preco_compras * (1 + 0.2)

print(f"Sua compra de R${preco_compras:.2f} vai custar R${preco_final:.2f} no final")
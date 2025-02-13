'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input("Valor da Casa: R$"))
salario_comprador = float(input("Salário do comprador: R$"))
anos_financiamento = int(input("Quantos anos de Financiamento: "))

valor_mensal = valor_casa / (anos_financiamento * 12)
limite_salario = salario_comprador * 0.3

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} anos a prestação será de R${valor_mensal:.2f}")

if valor_mensal <= limite_salario:
  print("Empréstimo pode ser CONCEDIDO")
else:
  print("Empréstimo NEGADO")
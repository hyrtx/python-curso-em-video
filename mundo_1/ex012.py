'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco_produto = float(input("Qual é o preço do produto? R$"))
desconto = 0.05
preco_desconto = round(preco_produto * (1-desconto), 2)

print(f"O produto que custava R${preco_produto}, na promoção com desconto de {desconto * 100:.0f}% vai custar R${preco_desconto}")
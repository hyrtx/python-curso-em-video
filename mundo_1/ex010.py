'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos 
dólares ela pode comprar.

Considere US$1.00 = R$3.27
'''

carteira = round(float(input("Quanto dinheiro você tem na carteira? R$")), 2)
dolar = 3.27
conversao = carteira / dolar

print(f"Com R${carteira} você pode comprar US${conversao:.2f}")
'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

valor_dia = 60
valor_km = 0.15

dias_alugados = int(input("Quantos dias alugados: "))
km_rodados = float(input("Quantos Km rodados: "))
valor_total = dias_alugados * valor_dia + km_rodados * valor_km

print(f"O total a pagar é de R${valor_total:.2f}")
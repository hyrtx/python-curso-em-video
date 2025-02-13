'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade_carro = int(input("Qual é a velocidade do carro? "))
valor_multa = 7

if velocidade_carro > 80:
  total_multa = (velocidade_carro - 80) * valor_multa
  print("MULTADO! Você excedeu o limite permitido de 80Km/h")
  print(f"Você deve pagar uma multa de R${total_multa:.2f}!")
else:
  print("Tenha um bom dia! Dirija com segurança!")
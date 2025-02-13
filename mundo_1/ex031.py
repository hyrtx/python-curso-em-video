'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para
viagens mais longas.
'''

distancia_viagem = float(input("Qual é a distância da sua viagem? "))

if distancia_viagem <= 200:
  preco_passagem = distancia_viagem * 0.5
else:
  preco_passagem = distancia_viagem * 0.45

print(f"Você está prestes a começar uma viagem de {distancia_viagem}Km.")
print(f"E o preço da sua passagem será de R${preco_passagem:.2f}")
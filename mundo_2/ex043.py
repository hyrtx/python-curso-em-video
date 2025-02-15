'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida
'''

peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))

imc = peso / altura ** 2

print(f"O IMC desta pessoa é {imc:.1f}")

if imc < 18.5:
  print("Esta pessoa está Abaixo do Peso")
elif imc < 25:
  print("Esta pessoa está no Peso Ideal!")
elif imc < 30:
  print("Esta pessoa está em condição de Sobrepeso")
elif imc < 40:
  print("Esta pessoa está em condição de Obesidade")
else:
  print("Esta pessoa está em condição de Obesidade Mórbida")
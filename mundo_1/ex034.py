'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario_funcionario = float(input("Qual é o salário do colaborador? "))

if salario_funcionario <= 1250:
  perc_aumento = 1.15
else:
  perc_aumento = 1.1

novo_salario = salario_funcionario * perc_aumento

print(f"Quem ganhava R${salario_funcionario:.2f} passa a ganhar R${novo_salario:.2f}.")
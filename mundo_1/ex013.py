'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario_funcionario = float(input("Qual é o salário do colaborador? R$"))
perc_aumento = 0.15
salario_reajustado = round(salario_funcionario * (1 + perc_aumento), 2)

print(f"Um funcionário que ganhava R${salario_funcionario}, com {perc_aumento * 100:.0f}% de aumento, passa a receber R${salario_reajustado}")
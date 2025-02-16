'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = input("Informe seu sexo: [M/F] ").strip().upper()

while sexo not in 'MF':
    sexo = input("Dados inválidos. Por favor, insira os dados corretos: [M/F] ").strip().upper()

print("Informação inputada com sucesso.")
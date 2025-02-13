'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

cidade = input("Em que cidade você nasceu: ").strip().upper()

validador_santo = cidade.split()[0] == 'SANTO'

print(validador_santo)
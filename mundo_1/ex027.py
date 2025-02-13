'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex.: Ana Maria de Souza.

Primeiro: Ana
Último: Souza
'''

nome = input("Digite seu nome completo: ").strip()

print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome.split()[0]}")
print(f"Seu último nome é {nome.split()[-1]}")
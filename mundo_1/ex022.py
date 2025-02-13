'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas e minúsculas;
Quantas letras tem ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome.
'''

nome = input("Digite seu nome completo: ").strip()

print("Analisando seu nome")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em maiúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome.replace(' ', ''))} letras")
print(f"Seu nome tem ao todo {len(nome.split()[0])} letras")
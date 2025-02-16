'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''

frase_palindromo = input("Digite uma palavra ou frase: ").strip().replace(" ", "").upper()
lista_frase_inversa = []

for p in frase_palindromo:
  lista_frase_inversa.append(p)

lista_frase_inversa.reverse()
frase_inversa = "".join(lista_frase_inversa)

print(f"O inverso de {frase_palindromo} é {frase_inversa}")

if frase_palindromo == frase_inversa:
  print("A frase digitada É UM PALÍNDROMO")
else:
  print("A frase digitada NÃO É UM PALÍNDROMO")
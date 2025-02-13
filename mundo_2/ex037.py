'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 para binário;
2 para octal;
3 para hexadecimal.
'''

lista_opcoes = ["BINÁRIO", "OCTAL", "HEXADECIMAL"]

numero = int(input("Digite um número inteiro: "))

while True:
  base_conversao = int(input("Escolha uma das bases para conversão:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL\n"))

  if base_conversao not in [1, 2, 3]:
    print("Digite uma base para conversão conforme instruções.")
  else:
    break

if base_conversao == 1:
  numero_convertido = bin(numero)
elif base_conversao == 2:
  numero_convertido = oct(numero)
else:
  numero_convertido = hex(numero)

print(f"Sua opção: {base_conversao}")
print(f"{numero} convertido para {lista_opcoes[base_conversao -1]} é igual a {numero_convertido}")
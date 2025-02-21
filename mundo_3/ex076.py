'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

tupla_produtos = ('Lápis', 1.75,
                  'Borracha', 2,
                  'Caderno', 15.9,
                  'Estojo', 25,
                  'Transferidor', 4.2,
                  'Compasso', 9.9,
                  'Mochila', 120.32,
                  'Canetas', 22.3,
                  'Livro', 34.9)

print("-" * 35)
print(f"{'LISTAGEM DE PREÇOS':^35}")
print("-" * 35)

for p, i in enumerate(tupla_produtos):
  if (p + 1) % 2 != 0:
    print(i + "." * (25 - len(i)) + "R$", end=' ')
  else:
    print(f"{i:>6.2f}")
print("-" * 35)
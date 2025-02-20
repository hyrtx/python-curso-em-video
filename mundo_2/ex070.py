'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:

qual é o total gasto na compra.
quantos produtos custam mais de R$1000.
qual é o nome do produto mais barato.
'''

produtos_list = []

while True:
  print("-=-" * 10)
  print("SUPERMERCADO")
  print("-=-" * 10)

  produto_info = {}
  produto_info['nome'] = input("Nome do produto: ").strip().upper()
  produto_info['preco'] = float(input("Preço do Produto: R$"))
  produtos_list.append(produto_info)

  continua_programa = input("Deseja continuar? [S/N]").strip().upper()[0]

  if continua_programa != 'S':
    print("-=-" * 10)
    print("ENCERRANDO PROGRAMA...\n")
    break

total_gasto_compras = sum(p['preco'] for p in produtos_list)
produtos_mais_1000_reais = sum(1 for p in produtos_list if p['preco'] > 1000)
nome_produto_mais_barato = min(
    (p for p in produtos_list),
    key= lambda p: p['preco'],
    default= None
)

print(f"O total da compra foi R${total_gasto_compras:.2f}")
print(f"Tiveram {produtos_mais_1000_reais} produtos com valor de mais de R$1000")
print(f"O produto mais barato foi {nome_produto_mais_barato['nome']}, custando R${nome_produto_mais_barato['preco']:.2f}")
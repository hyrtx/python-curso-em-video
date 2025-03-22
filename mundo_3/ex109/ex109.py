import moeda

preco = float(input("Digite o preço: R$"))
preco_formatado = moeda.moeda(preco)

print(f"O dobro de {preco_formatado} é {moeda.dobro(preco, True)}")
print(f"A metade de {preco_formatado} é {moeda.moeda(preco, True)}")
print(f"Aumentando 10%, {preco_formatado} passa a ser {moeda.aumentar(preco, True)}")
print(f"Descontando 10%, {preco_formatado} passa a ser {moeda.diminuir(preco, True)}")
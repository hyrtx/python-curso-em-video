import moeda

preco = float(input("Digite o preço: R$"))

print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"Aumentando 10%, {moeda.moeda(preco)} passa a ser {moeda.moeda(moeda.aumentar(preco))}")
print(f"Descontando 10%, {moeda.moeda(preco)} passa a ser {moeda.moeda(moeda.diminuir(preco))}")
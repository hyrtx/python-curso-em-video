import moeda

preco = float(input("Digite o preço: R$"))

print(f"O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}")
print(f"A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}")
print(f"Aumentando 10%, R${preco:.2f} passa a ser R${moeda.aumentar(preco):.2f}")
print(f"Descontando 10%, R${preco:.2f} passa a ser R${moeda.diminuir(preco):.2f}")
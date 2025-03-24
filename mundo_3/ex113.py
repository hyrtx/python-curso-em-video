def valorinteiro():
    while True:
        valor = input("Digite um valor inteiro: ")

        try:
            return int(valor)
        except ValueError:
            print(f"ERRO! {valor} não é um número inteiro. Tente novamente.")

def valorreal():
    while True:
        valor = input("Digite um valor real: ").strip().replace(',', '.')

        try:
            return float(valor)
        except ValueError:
            print(f"ERRO! {valor} não é um número real válido. Tente novamente.")

num_inteiro = valorinteiro()
num_real = valorreal()
print(f"O valor inteiro digitado foi {num_inteiro} e o valor real foi {num_real}")
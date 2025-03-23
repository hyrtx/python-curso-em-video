def leiadinheiro() -> float:
    '''
    Lê um valor monetário válido do usuário, convertendo para float.

    Retorno
    -------
    Valor validado e formatado em float
    '''

    while True:
        dinheiro = input("Digite o preço: R$").strip().replace(',', '.')

        try:
            return float(dinheiro)
        except ValueError:
            print(f"ERRO! {dinheiro} não é um valor monetário válido. Tente novamente.")
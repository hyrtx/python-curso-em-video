def moeda(valor: float) -> str:
    '''
    Função que formata o um valor em float em moeda (R$#,##)

    Parâmetros
    ----------
    valor: Recebe o valor que será formatado
    
    Retorno
    -------
    valor em string no formato R$#,##
    '''

    valor_formatado = f'R${valor:.2f}'
    return valor_formatado

def aumentar(valor: float, perc_aumento: float = 0.1, formatar: bool = False) -> float | str:
    '''
    Função que adiciona o percentual passado ao valor digitado

    Parâmetros
    ----------
    valor: Recebe o valor a ser adicionado os 10%.
    perc_aumento: (Opcional) Percentual que será adicionado ao valor. Tem por padrão 10%.
    formatar: (Opcional) Indica se o valor deve ser formatado em moeda, onde True formata.
    
    Retorno
    -------
    Valor com o percentual a adicionar já aplicado
    '''

    if formatar:
        return moeda(valor * (1 + perc_aumento / 100))
    else:
        return valor * (1 + perc_aumento / 100)

def diminuir(valor: float, perc_reducao: float = 0.1, formatar: bool = False) -> float | str:
    '''
    Função que reduz o percentual passado do valor digitado

    Parâmetros
    ----------
    valor: Recebe o valor que terá a redução.
    perc_reducao: (Opcional) Percentual que será reduzido do valor. Tem por padrão 10%.
    formatar: (Opcional) Indica se o valor deve ser formatado em moeda, onde True formata.
    
    Retorno
    -------
    Valor com o percentual de redução aplicado
    '''

    if formatar:
        return moeda(valor * (1 - perc_reducao / 100))
    else:
        return valor * (1 - perc_reducao / 100)

def dobro(valor: float, formatar: bool = False) -> float | str:
    '''
    Função que dobra o valor digitado

    Parâmetros
    ----------
    valor: Recebe o valor que será dobrado.
    formatar: (Opcional) Indica se o valor deve ser formatado em moeda, onde True formata.
    
    Retorno
    -------
    valor multiplicado por 2
    '''
    
    if formatar:
        return moeda(valor * 2)
    else:
        return valor * 2

def metade(valor: float, formatar: bool = False) -> float | str:
    '''
    Função que divide em dois o valor digitado

    Parâmetros
    ----------
    valor: Recebe o valor que será dividido.
    formatar: (Opcional) Indica se o valor deve ser formatado em moeda, onde True formata.
    
    Retorno
    -------
    valor dividido por 2
    '''
    
    if formatar:
        return moeda(valor / 2)
    else:
        return valor / 2
    

def resumo(valor: float, p_aumento: float, p_diminuir: float) -> None:
    '''
    Função que trás o dobro, metade e o aumento e redução do valor com base nos percentuais escolhidos

    Parâmetros
    ----------
    :valor: Recebe o valor que será dividido.
    :p_aumento: Percentual de aumento do valor
    :p_diminuir: Percentual de redução do valor
    
    Retorno
    -------
    Nenhum
    '''

    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)

    print(f"Preço analisado: {moeda(valor):>13}")
    print(f"Dobro do preço: {dobro(valor, True):>14}")
    print(f"Metade do preço: {metade(valor, True):>13}")
    print(f"{p_aumento}% de aumento: {aumentar(valor, p_aumento, True):>14}")
    print(f"{p_diminuir}% de redução: {diminuir(valor, p_diminuir, True):>14}")

    print("-" * 30)
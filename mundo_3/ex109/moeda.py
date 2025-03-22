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

def aumentar(valor: float, formatar: bool = False) -> float | str:
    '''
    Função que adiciona 10% no valor digitado

    Parâmetros
    ----------
    valor: Recebe o valor a ser adicionado os 10%.
    formatar: (Opcional) Indica se o valor deve ser formatado em moeda, onde True formata.
    
    Retorno
    -------
    valor + 10% do valor original acrescentado
    '''

    if formatar:
        return moeda(valor * 1.1)
    else:
        return valor * 1.1

def diminuir(valor: float, formatar: bool = False) -> float | str:
    '''
    Função que reduz 10% do valor digitado

    Parâmetros
    ----------
    valor: Recebe o valor a ser reduzido os 10%.
    formatar: (Opcional) Indica se o valor deve ser formatado em moeda, onde True formata.
    
    Retorno
    -------
    valor - 10% do valor original reduzido
    '''

    if formatar:
        return moeda(valor * 0.9)
    else:
        return valor * 0.9

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
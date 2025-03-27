from sistema import config

# Funções visuais
def linha() -> None:
    print("-" * 40)

def titulo(texto: str) -> None:
    linha()
    print(texto.center(40))
    linha()

def opcoes(opcoes: list) -> None:
    for p, v in enumerate(opcoes):
        print(f"\033[33m{p + 1}\033[m - \033[34m{v}\033[m")

# Impressão do menu e opções
def menu() -> int:
    titulo("MENU PRINCIPAL")
    opcoes(config.opcoes_menu)
    linha()
    opcao = config.valid_opcoes_menu("Escolha uma opção: ")
    return opcao
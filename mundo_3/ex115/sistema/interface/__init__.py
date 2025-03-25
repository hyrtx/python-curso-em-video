from sistema import config

# Visuais da interface

def linha():
    print("-" * 40)

def titulo(texto: str):
    linha()
    print(texto.center(40))
    linha()

def opcoes(opcoes: list):
    for p, v in enumerate(opcoes):
        print(f"\033[33m{p + 1}\033[m - \033[34m{v}\033[m")

def menu():
    titulo("MENU PRINCIPAL")
    opcoes(config.opcoes_menu)
    linha()
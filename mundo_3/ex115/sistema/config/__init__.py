opcoes_menu = [
    "Cadastrar pessoas",
    "Ver pessoas cadastradas",
    "Sair do sistema"
]

def valid_opcoes_menu(msg: str) -> int:

    while True:
        valor = input(msg)

        try:
            valor = int(valor)

            if 1 <= valor <= len(opcoes_menu):
                return valor
            else:
                print("\033[31mERRO! Digite uma das opções presentes no menu!\033[m")
                continue
         
        except ValueError:
            print("\033[31mERRO! Digite apenas valores numéricos correspondentes as opções dadas no menu!\033[m")
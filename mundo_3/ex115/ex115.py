from sistema import interface, config

while True:
    opcao_menu = interface.menu()
    interface.titulo(config.opcoes_menu[opcao_menu - 1])

    if opcao_menu == 3:
        interface.titulo("Saindo do sistema... Até logo!")
        break
    else:
        interface.titulo(config.opcoes_menu[opcao_menu - 1])
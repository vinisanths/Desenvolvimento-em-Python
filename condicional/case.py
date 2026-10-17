print("========== MENU DE INSCRIÇÃO DA MARATONA ===========")
print("1 - Maratona Completa")
print("2 - Meia Maratona")
print("3 - Corrida de Estreia")
opcao = int(input("Escolha o  número que desaja concorrer: "))
print("\n------------Resultado------------")
match opcao:
    case 1:
        print("Inscrição Confirmada: Maratona Completa (42.195 KM)")
    case 2:
        print("Inscrição Confirmada: Meia Maratona (21.097 KM)")
    case 3:
        print("Inscrição Confirmada: Corrida de Estreia (5 KM)")
    case _:
        print("Erro: Categoria Inexistente! Escolha de 1 a 3.") 
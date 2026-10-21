#Calculaddora
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma opção: "))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        print("Resultado:", n1 + n2)
    case 2:
        print("Resultado:", n1 - n2)
    case 3:
        print("Resultado:", n1 * n2)
    case 4:
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Não é possível dividir por zero.")
    case _:
        print("Opção inválida.")
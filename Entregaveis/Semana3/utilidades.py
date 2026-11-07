# Módulo com as funções

def converter_temperatura(celsius):
    return (celsius * 9 / 5) + 32

def validar_senha(senha):
    if len(senha) >= 8:
        return True
    return False

def calcular_total(*precos):
    total = 0
    for preco in precos:
        total = total + preco
    return total

def ficha_aluno(**dados):
    print("Ficha do aluno:")
    for chave, valor in dados.items():
        print(chave, ":", valor)
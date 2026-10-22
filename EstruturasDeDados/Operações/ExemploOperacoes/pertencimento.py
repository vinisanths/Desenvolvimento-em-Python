def existe(estoque, produto):
    #O operador devolve True/False
    return produto in estoque

if __name__ == "__main__":
    lista = ["Mouse", "Teclado"]
    if existe(lista, "Mouse"):
        print("Já cadastrado")
    else:
        print("POde Comprar")
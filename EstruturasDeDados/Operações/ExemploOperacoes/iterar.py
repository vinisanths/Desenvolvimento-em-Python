def iterar(estoque):
    #Enumerate da indice e valor
    for i, produto in enumerate(estoque, start=1):
        print(i, "-", produto)
    print("Total: ", len(estoque))

if __name__ == "__main__":
    iterar(["Mouse", "Teclado"])
def atualizar(estoque, antigo, novo):
    #Localiza o indice do produto
    if antigo in estoque:
        i = estoque.index(antigo)
        estoque[i] = novo #Faz a substituição
    return estoque

if __name__ == "__main__":
    print(atualizar(["Mose"], "Mose", "Mouse"))
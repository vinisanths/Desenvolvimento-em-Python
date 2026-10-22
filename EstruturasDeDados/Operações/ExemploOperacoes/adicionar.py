def adicionar(estoque, produto):
    #Evita duplicidade no estoque
    if produto not in estoque: #Verifica se o produto já esta no etoque
        estoque.append(produto) #Insere o produto no estoque 
    return estoque

if __name__ == "__main__":
    print(adicionar(["Mouse"], "Teclado"))
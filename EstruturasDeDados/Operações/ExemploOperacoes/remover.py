def remover(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
    else:
        print(f"Produto: {produto} não encontrado")
    return estoque

if __name__ == "__main__":
    print(remover(["Mouse", "hd"], "hd"))
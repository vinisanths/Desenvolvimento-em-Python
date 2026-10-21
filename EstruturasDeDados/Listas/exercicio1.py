"""
Supermercado - Registrar preços e calcular total
"""
totalItens = int(input("Digite a quantidade de itens a serem adicionados: "))
precos = []
for i in range(totalItens):
    preco = int(input(f"Digite o valor do {i+1}° produto: "))
    #Lista com os preços dos produtos
    precos.insert(i, preco)
    #Soma todos os itens da lista
    total = sum(precos)
    #Exibe o valor total da compra
print(f"Total dos itens: {totalItens}, valor total da Compra: {total}") 